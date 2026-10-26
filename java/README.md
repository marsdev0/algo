# Java 刷题模块

与 Python 侧（`src/algo/`）按同样的 topic 分包，一题一文件，方便对照复习。

## IDE 双开（推荐）

- **PyCharm** 打开仓库根目录（Python 侧，uv 管理）
- **IntelliJ IDEA**（Community 即可，免费）单独打开本 `java/` 目录

两个 IDE 的 `.idea` 配置分别在 `java/.idea` 和根目录 `./.idea`，互不干扰，
macOS 上 `Cmd + Tab` 即可切换窗口。

## 目录约定

```
java/
├── pom.xml                              # Maven, JDK 21
└── src/
    ├── main/java/algo/<topic>/Xxx.java  # 一题一个类
    └── test/java/algo/<topic>/XxxTest.java  # 可选的对拍测试
```

## 常用命令

```bash
cd java
mvn test                 # 跑全部测试
mvn test -Dtest=ClimbingStairsTest   # 跑单个测试
```

IDEA 里直接点类名旁边的绿色三角即可运行 `main` 或测试。
