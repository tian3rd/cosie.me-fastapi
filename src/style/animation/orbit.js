// CONFIGURE ORBIT ANIMATION AND TOOLTIP

document.addEventListener("DOMContentLoaded", () => {
  const icons = Array.from(document.querySelectorAll(".orbit-circle"));
  const orbitCenter = document.getElementById("orbit-center");

  // Orbit definition (angle start, radius)
  const orbitData = [
    { angle: 15, radius: 0.212 },
    { angle: 255, radius: 0.212 },
    { angle: 112, radius: 0.327 },
    { angle: 330, radius: 0.327 },
    { angle: 150, radius: 0.442 },
    { angle: 205, radius: 0.442 },
    { angle: 42, radius: 0.442 },
  ];

  let t0 = Date.now();
  function animate() {
    // How many degrees per second
    const SPEED = 9; // deg/sec: slow and smooth
    const t = (Date.now() - t0) / 1000;

    // Get the current size of the orbit-center div
    const { width, height } = orbitCenter.getBoundingClientRect();
    const centerX = width / 2;
    const centerY = height / 2;

    icons.forEach((icon, i) => {
      const { angle, radius } = orbitData[i % orbitData.length];
      const theta = (((angle + t * SPEED) % 360) * Math.PI) / 180;
      const cx = centerX + Math.cos(theta) * radius * width;
      const cy = centerY + Math.sin(theta) * radius * height;
      icon.style.left = `${cx}px`;
      icon.style.top = `${cy}px`;
    });
    requestAnimationFrame(animate);
  }
  animate();

  // Tooltip is handled by CSS (hover). You can add touch/mouseover support here if needed.
});
