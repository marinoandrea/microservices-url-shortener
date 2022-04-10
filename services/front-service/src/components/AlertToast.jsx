import React from "react";

const FADE_OUT_TIMEOUT_MS = 5000;

const AlertToast = ({ errorTimestamp, error }) => {
  const [displayAlert, setDisplayAlert] = React.useState(false);

  React.useEffect(() => {
    const interval = setInterval(() => {
      const elapsed = Date.now() - errorTimestamp;
      setDisplayAlert(elapsed <= FADE_OUT_TIMEOUT_MS);
    }, 250);

    return () => {
      clearInterval(interval);
    };
  }, [errorTimestamp]);

  return (
    <div
      className="alert alert-danger"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      style={{
        position: "absolute",
        top: 0,
        right: 0,
        left: 0,
        margin: "auto",
        zIndex: 1000,
        maxWidth: 450,
        opacity: displayAlert ? 100 : 0,
        pointerEvents: displayAlert ? "all" : "none",
      }}
    >
      {error}
    </div>
  );
};

export default AlertToast;
