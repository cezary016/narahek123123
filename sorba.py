
import org.junit.jupiter.api.Test;
import picocli.CommandLine;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/**
 * Basic functional/integration tests of {@code wallet-tool}
 */
public class WalletToolTest {

    @Test
    void canConstruct() {
        WalletTool walletTool = new WalletTool();

        assertNotNull(walletTool);
    }

    @Test
    void noArgsFails() {
        int exitCode = execute();

        assertEquals(2, exitCode);
    }

    @Test
    void emptyStringArgFails() {
        int exitCode = execute("");

        assertEquals(1, exitCode);
    }
