# SDD.TW BDD Experiments

《臺灣規格驅動開發研究組織 (SDD.TW)》是一場由《水球軟體學院》發起的技術研究社群，目標是集結全台具備軟體開發能力的工程師，共同推進 AI × SDD/BDD 開發流程的研究與實踐。

> 「如果大家都關注 AI x SDD/BDD 這件事，台灣軟工進度就有機會超前國外；當國外 AI 軟工都只會寫 rules 時，我們就已經全部都在寫 spec，產值絕對爆增。」

## 本組織將專注於以下目標

1. 本組織相信 AI x SDD/BDD 的方法，一定能讓 AI 在背景就產出 80%~90% 可靠且正確的程式，而這一定是未來 Vibe Coding 的趨勢，你一定是想要追求最前沿的軟工技術才加入本組織。
2. 組織規劃好了初步研究藍圖，分為底下三大路線
    a. 開發流程全自動化（後端）— Feature file (BDD) 到 API Spec/ERD 到程式
    b. 開發流程全自動化（前端）— 線框 到 User-flow (BDD) 到程式
    c. 回饋流程智能化 (全端) — 前後端整合自動化建立新的驗收測試
這三者只要都研究完成，那 Vibe Coding 才算是成熟，軟體工程師能與與 AI 「平行」合作帶來百倍產出，故稱「AI 百倍軟工研究組織」。

## 歡迎所有人參與

你的參與，不僅代表你願意走在 AI 軟體開發方法論的最前線，更代表你願意投身於一場嚴謹、務實、強調產出價值與技術驗證的研究歷程（所有的研究紀錄都會使用 Github Repository 保存脈絡）。

### 報名方法

1. 加入水球軟體學院 Discord：<https://discord.gg/uWGTF7RSnW>
2. 照著此 Discord 社群內 #加入研究計劃 置頂訊息的指示進行即可成功報名
若你已準備好成為推動 AI × SDD/BDD 開發方法的革新者，誠摯邀請你完成報名，與來自全台的技術夥伴攜手共創。

---

## BDD Benchmarks

本專案包含多個 BDD 實驗基準測試，用於驗證和學習 Behavior-Driven Development 方法論。

### Benchmark 列表

#### 1. Order Pricing System (`benchmarks/order-pricing/`)

電商訂單定價系統，包含多種促銷策略。

**功能特色**:

- 門檻折扣 (Threshold Discount)
- 化妝品買一送一 (Buy-One-Get-One)
- 雙十一批量優惠 (Double Eleven Promotion)
- 多重促銷疊加

**測試覆蓋**: 2 features, 10 scenarios, 42 test steps

[→ 查看詳情](benchmarks/order-pricing/README.md)

#### 2. Chinese Chess (`benchmarks/chinese-chess/`)

中國象棋遊戲邏輯實作，完整實現所有棋子規則與勝負判定。

**功能特色**:

- 七種棋子完整規則: 將/帥、士/仕、車、馬/傌、炮、相/象、兵/卒
- 九宮限制 (General and Guard movement within palace)
- 河界限制 (Elephant cannot cross river, Soldier behavior changes)
- 蹩馬腿 (Horse can be blocked)
- 炮架子 (Cannon must jump one piece to capture)
- 將帥對臉禁止 (Generals cannot face each other)
- 勝負判定 (Capturing General wins immediately)

**測試覆蓋**: 1 feature, 22 scenarios, 66 test steps

[→ 查看詳情](benchmarks/chinese-chess/tasks/)

### 專案結構

```markdown
bdd-trials/
├── benchmarks/
│   ├── order-pricing/       # 電商定價系統
│   │   ├── src/             # 原始碼
│   │   ├── features/        # BDD 測試場景
│   │   ├── tasks/           # 需求與設計文件
│   │   └── README.md
│   │
│   └── chinese-chess/       # 中國象棋
│       ├── src/             # 原始碼 (entities, pieces, game)
│       ├── features/        # BDD 測試場景
│       └── tasks/           # 需求與設計文件 (ERD, OOD)
│
├── requirements.txt         # 共用依賴
├── pyproject.toml          # 共用配置
└── README.md               # 本檔案
```

### BDD 開發方法論

所有 benchmarks 嚴格遵守 BDD 原則：

1. **Red-Green-Refactor 循環**
   - Red: 先寫失敗的測試
   - Green: 實作最小程式碼使測試通過
   - Refactor: 重構程式碼同時保持測試通過

2. **一次一個 Scenario**
   - 循序實作每個 scenario
   - 使用 `@skip` 標記待實作的 scenarios
   - 絕不跳過 Red 或 Refactor 階段

3. **測試先行開發**
   - 沒有失敗的測試就不寫實作
   - 驗證測試確實執行且正確失敗
   - 每個階段後檢查測試數量

### 技術棧

- **語言**: Python 3.11
- **BDD 框架**: Behave 1.2.6
- **程式碼格式化**: Black (line-length=79)

### 快速開始

```bash
# 安裝依賴
pip install -r requirements.txt

# 執行特定 benchmark
cd benchmarks/order-pricing
behave --no-capture

# 格式化程式碼
black benchmarks/
```
