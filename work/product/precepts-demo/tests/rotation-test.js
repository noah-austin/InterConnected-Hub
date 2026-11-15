// Stress-test the prayer chain rotation using the app's own functions (callee, nextWeek, joinChain, leaveChain).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome' });
  const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + process.argv[2]);
  const result = await p.evaluate(() => {
    const out = { sizes: [], problems: [] };
    // 1) Every size from 1 to 40, three full rotations each
    for (let n = 1; n <= 40; n++) {
      const ids = Array.from({ length: n }, (_, i) => 'm' + i);
      S.chain.sat = ids.slice(); S.shift.sat = 1;
      const weeks = 3 * Math.max(1, n - 1);
      const seen = ids.map(() => new Set());
      let self = 0, missedCall = 0, doubleCalled = 0;
      for (let w = 0; w < weeks; w++) {
        const calledCount = {};
        for (let i = 0; i < n; i++) {
          const c = callee('sat', i);
          if (n >= 2 && c === ids[i]) self++;
          if (c == null) missedCall++;
          calledCount[c] = (calledCount[c] || 0) + 1;
          if (n >= 2 && w < n - 1) seen[i].add(c);
        }
        if (n >= 2 && Object.values(calledCount).some(v => v !== 1)) doubleCalled++;
        nextWeek('sat');
      }
      const coversAll = n < 2 || seen.every(s => s.size === n - 1);
      const row = { n, odd: n % 2 === 1, weeks, selfCalls: self, weeksSomeoneCalledTwiceOrNot: doubleCalled, everyManCallsEveryOtherOncePerCycle: coversAll };
      out.sizes.push(row);
      if (self || doubleCalled || !coversAll || missedCall) out.problems.push(row);
    }
    // 2) Men joining and leaving mid-rotation (odd and even counts back and forth), 5,000 random steps
    const pool = Array.from({ length: 30 }, (_, i) => 'p' + i);
    pool.forEach(id => { men[id] = { id, name: id, group: 'sat', inChain: false, initials: 'P', color: '#000', phone: '' }; });
    S.chain.sat = pool.slice(0, 7); S.chain.sat.forEach(id => men[id].inChain = true); S.shift.sat = 1;
    let churnSelf = 0, churnBad = 0, minN = 99, maxN = 0;
    let seed = 12345; const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
    for (let step = 0; step < 5000; step++) {
      const r = rnd(), C = S.chain.sat;
      // Men ask to join or leave any day; the change lands at the automated Saturday move.
      if (r < 0.3) { const out_ = pool.filter(id => !wantsChain(id)); if (out_.length) setChainWish(out_[Math.floor(rnd() * out_.length)], true); }
      else if (r < 0.55) { const in_ = pool.filter(id => wantsChain(id)); if (in_.length > 2) setChainWish(in_[Math.floor(rnd() * in_.length)], false); }
      else saturdayMorning();
      const n = S.chain.sat.length; minN = Math.min(minN, n); maxN = Math.max(maxN, n);
      const counts = {};
      for (let i = 0; i < n; i++) { const c = callee('sat', i); if (c === S.chain.sat[i]) churnSelf++; counts[c] = (counts[c] || 0) + 1; }
      if (n >= 2 && Object.values(counts).some(v => v !== 1)) churnBad++;
      if (S.shift.sat < 1 || S.shift.sat > n - 1) churnBad++;
    }
    out.churn = { steps: 5000, chainSizeRange: [minN, maxN], selfCalls: churnSelf, brokenWeeks: churnBad };
    // 3) Men removed from the group mid-week (gap closed until Saturday), mixed with joins, leaves and Saturdays
    let rmBad = 0, rmSelf = 0, rmCount = 0, rebuilt = 0;
    for (let step = 0; step < 5000; step++) {
      const r = rnd(), live = pool.filter(id => !men[id].removed && men[id].inChain);
      if (r < 0.2) { if (live.length > 1) { rmCount++; if (removeFromGroup(live[Math.floor(rnd() * live.length)]).rebuilt) rebuilt++; } }
      else if (r < 0.45) { const out_ = pool.filter(id => !men[id].removed && !wantsChain(id)); if (out_.length) setChainWish(out_[Math.floor(rnd() * out_.length)], true); }
      else if (r < 0.55) { pool.filter(id => men[id].removed && !men[id].inChain).forEach(id => { men[id].removed = false; }); } // men re-added to the group
      else saturdayMorning();
      // Check: every man still in the chain (not removed) calls exactly one other such man, and is called by exactly one.
      const C = S.chain.sat, counts = {}; let callers = 0;
      const liveN = C.filter(id => !men[id].removed).length; // a chain of one man has nobody to call; that's not a self-call
      C.forEach((id, i) => { if (men[id].removed || liveN < 2) return; const c = callee('sat', i); callers++; if (c === id) rmSelf++; if (men[c].removed) rmBad++; counts[c] = (counts[c] || 0) + 1; });
      if (callers >= 2 && (Object.keys(counts).length !== callers || Object.values(counts).some(v => v !== 1))) rmBad++;
    }
    out.removals = { steps: 5000, removals: rmCount, rebuiltInstead: rebuilt, selfCalls: rmSelf, brokenWeeks: rmBad };
    return out;
  });
  console.log('size  odd/even  weeks  self-calls  bad-weeks  covers-everyone');
  result.sizes.forEach(r => console.log(String(r.n).padStart(4), r.odd ? '  odd    ' : '  even   ', String(r.weeks).padStart(5), String(r.selfCalls).padStart(11), String(r.weeksSomeoneCalledTwiceOrNot).padStart(10), '  ', r.everyManCallsEveryOtherOncePerCycle));
  console.log('PROBLEMS:', JSON.stringify(result.problems));
  console.log('CHURN:', JSON.stringify(result.churn));
  console.log('REMOVALS:', JSON.stringify(result.removals));
  console.log('ERRORS:', JSON.stringify(errs));
  await b.close();
})();
