---
title: 'Analogical Deep Research: Retrieving and Integrating Historical Analogies
  for Foresight Analysis'
title_zh: 类比深度研究：面向前瞻分析的历史类比检索与整合框架
authors:
- Yongqiang Chen
- Guangyi Chen
- Yuewen Sun
- Kun Zhang
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Carnegie Mellon University
arxiv_id: '2607.13602'
url: https://arxiv.org/abs/2607.13602
pdf_url: https://arxiv.org/pdf/2607.13602
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 前瞻推理·历史类比优化
tags:
- LLM Agent
- Analogical Reasoning
- Causal Representation
- Foresight Analysis
- Deep Research
one_liner: 提出类比深度研究任务与基准，因果驱动的CANA Agent类比推理能力较SOTA提升超10%
practical_value: '- 做用户行为/行业趋势预测类Agent时，可借鉴事件结构分解（前置条件/时间链/机制/结果）替代表面文本匹配，提升历史相似事件召回准确率，比如电商大促效果预测时找历史同机制大促案例，避免只看GMV等表面指标匹配

  - 做决策类Agent的推理验证模块时，可复用跨类比确认原则：核心推断结论需至少2个独立历史案例支撑，降低单案例巧合导致的决策偏差，比如新品冷启动销量预测时，多品类相似案例交叉验证提升结论可信度

  - 可将CANA作为轻量化插件嵌入现有深度研究Agent框架，仅需额外生成结构类比简报作为上下文输入，无需重构原有Agent架构即可提升推理深度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有深度研究（DR）Agent做前瞻分析时依赖表面特征匹配，无法找到深层机制相似的历史类比事件，导致预测/分析结论缺乏历史依据、偏差大；而人类专家用结构化历史类比能将冲突预测准确率从32%提升至60%，亟需让Agent具备机制级的历史类比检索与整合能力。

### 方法关键点
- 定义类比深度研究（ADR）任务，提出两条核心原则：1）类比检索基于事件的机制级因果结构表示而非表面描述；2）核心结构位置需至少2个独立类比事件交叉验证，降低巧合概率
- 提出因果类比研究员框架CANA：1）将所有事件分解为前置条件、时间链、核心机制、结果的结构化表示；2）迭代检索类比事件，直到每个隐藏结构位置都有≥2个独立事件支撑；3）生成结构类比简报作为额外上下文输入主流DR Agent
- 构建首个ADR-bench基准，包含15个跨金融、地缘、科技领域的事件，其中10个有文献标注的历史类比，5个正在发生的前瞻事件

### 关键结果
对比OpenAI DR、Gemini DR、Qwen DR等商用DR Agent，以及vanilla MiroFlow Agent：1）CANA将历史类比生成效果提升最高10%，弱基模型Qwen3-8B加CANA可超过GPT-5.4-mini原生自反射方法；2）ADR-bench上所有商用Agent的隐藏因子识别率为0，CANA+Claude 4.5可识别13/22个历史事件隐藏因子、3/20个前瞻事件隐藏因子；3）CANA的机制锚定声明占比最高达94%，远超商用Agent的不足20%。

最值得记住的一句话：仅靠表面特征匹配无法识别事件的隐藏因果结构，机制对齐+跨类比验证是用历史类比提升Agent前瞻推理能力的核心路径。
