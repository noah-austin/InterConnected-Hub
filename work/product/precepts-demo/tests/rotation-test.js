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
      if (r < 0.3) { const out_ = pool.filter(id => !men[id].inChain); if (out_.length) joinChain(out_[Math.floor(rnd() * out_.length)]); }
      else if (r < 0.55) { if (C.length > 2) leaveChain(C[Math.floor(rnd() * C.length)]); }
      else nextWeek('sat');
      const n = S.chain.sat.length; minN = Math.min(minN, n); maxN = Math.max(maxN, n);
      const counts = {};
      for (let i = 0; i < n; i++) { const c = callee('sat', i); if (c === S.chain.sat[i]) churnSelf++; counts[c] = (counts[c] || 0) + 1; }
      if (n >= 2 && Object.values(counts).some(v => v !== 1)) churnBad++;
      if (S.shift.sat < 1 || S.shift.sat > n - 1) churnBad++;
    }
    out.churn = { steps: 5000, chainSizeRange: [minN, maxN], selfCalls: churnSelf, brokenWeeks: churnBad };
    return out;
  });
  console.log('size  odd/even  weeks  self-calls  bad-weeks  covers-everyone');
  result.sizes.forEach(r => console.log(String(r.n).padStart(4), r.odd ? '  odd    ' : '  even   ', String(r.weeks).padStart(5), String(r.selfCalls).padStart(11), String(r.weeksSomeoneCalledTwiceOrNot).padStart(10), '  ', r.everyManCallsEveryOtherOncePerCycle));
  console.log('PROBLEMS:', JSON.stringify(result.problems));
  console.log('CHURN:', JSON.stringify(result.churn));
  console.log('ERRORS:', JSON.stringify(errs));
  await b.close();
})();
