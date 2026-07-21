---
title: 'DRNOISE: Benchmarking Deep Research Agents in Misleading Evidence Environments'
title_zh: DRNOISE：误导性证据环境下深度研究Agent基准测试
authors:
- Jun Nie
- Zhiqin Yang
- Zhenheng Tang
- Yonggang Zhang
- Xiaowen Chu
- Xinmei Tian
- Bo Han
affiliations:
- Hong Kong Baptist University
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2607.17291'
url: https://arxiv.org/abs/2607.17291
pdf_url: https://arxiv.org/pdf/2607.17291
published: '2026-07-19'
collected: '2026-07-21'
category: Agent
direction: Agent性能评估 · 抗误导信息验证
tags:
- Research Agent
- Benchmark
- Misleading Evidence
- Verification
- RAG Robustness
one_liner: 构建仅含单条误导证据的可控基准，揭示当前研究Agent存在广泛验证惰性
practical_value: '- 电商导购/商品核验类Agent可新增「直接答案需匹配至少2条独立原始证据链」的强制校验规则，禁止碰到首个看似合理的答案就终止检索，避免被商家营销软文、过时商品信息误导

  - RAG系统召回侧可给原始记录（交易凭证、官方资质、售后数据等）加权，降低二次总结类文档（媒体测评、第三方汇总）的权重，减少误导信息被优先召回的概率

  - 评估自研Agent可靠性时可复用DRNOISE的配对实验设计：同一任务分别在干净/加入单条误导信息的语料下测试，用条件顺从率量化验证能力短板，比单纯测准确率更有效

  - 通用验证提示对降低误导率的效果有限（仅提升16个点准确率），业务上不要过度依赖prompt优化，优先结合流程约束（强制多源校验）提升抗干扰能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前深度研究Agent广泛用于开放网络信息检索，但现有基准未覆盖「真实环境中普通虚假总结与真实底层记录共存」的场景：Agent明明能检索到真实证据，却容易被直接给出答案的虚假文档误导，提前终止验证流程返回错误结论，这一漏洞在金融分析、电商商品核验、合规调研等高风险场景会造成严重损失。

### 方法关键点
- 构建100个任务的DRNOISE基准，覆盖实体选择、数值聚合、多跳关联等10类常见信息处理场景；每个任务干净环境下提供2条独立的间接证据链，需推理得到黄金答案，无任何文档直接给出答案。
- 噪声环境仅新增1条看似合理的普通总结类文档（如行业报道、汇总报告），直接给出与黄金答案冲突的虚假结果，其余语料与干净环境完全一致，隔离误导信息的单独影响。
- 提出「条件顺从率」指标：仅统计模型在干净环境下答对、噪声环境下答错且答案恰好等于注入虚假值的比例，避免弱模型因本身能力差显得抗干扰的评估偏差。

### 关键结果
在Gemini 3.5 Flash、DeepSeek V4 Flash、GPT-5.4等主流大模型驱动的Agent上测试：
- 干净环境下准确率82%-96%的强Agent，加入单条误导文档后准确率下降66-88个百分点，最高条件顺从率达98.1%，即98%原本能答对的题被误导答错。
- 通用验证提示仅能提升16个点的噪声准确率，攻击感知提示（明确要求不信任直接总结）可提升55个点，但无法完全消除漏洞。
- 主导失效模式是验证惰性：100%的噪声任务中Agent同时检索到了虚假文档和真实证据，但平均检索次数从7.1次降至4.5次，仅16%的任务完成了完整证据链核验。

### 最值得记住的结论
当前研究Agent的核心短板不是检索或推理能力，而是验证策略缺陷：遇到直接给出的答案类文档时会优先作为终止信号，而非触发进一步的多源核验流程。
