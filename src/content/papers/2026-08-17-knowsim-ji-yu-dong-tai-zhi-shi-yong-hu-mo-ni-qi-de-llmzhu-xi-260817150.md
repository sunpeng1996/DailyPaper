---
title: 'KnowSim: Evaluating Information Calibration in LLM Assistants with User Simulators
  that Learn'
title_zh: KnowSim：基于动态知识用户模拟器的LLM助手信息校准评估框架
authors:
- Yoonjoo Lee
- Hyoungwook Jin
- Tae Soo Kim
- Shaoyang Zhang
- Philippe Laban
- Q. Vera Liao
affiliations:
- University of Michigan
- KAIST
- Microsoft Research
arxiv_id: '2608.17150'
url: https://arxiv.org/abs/2608.17150
pdf_url: https://arxiv.org/pdf/2608.17150
published: '2026-08-17'
collected: '2026-08-19'
category: Eval
direction: LLM评估 · 知识感知用户模拟器
tags:
- User Simulator
- Information Calibration
- Knowledge State
- LLM Evaluation
- Multi-turn Dialogue
one_liner: 提出带动态知识状态的用户模拟器，可量化LLM对不同认知用户的信息校准效果
practical_value: '- 做电商LLM导购/客服Agent开发时，可借鉴IU概念图+动态知识状态的设计，量化用户对商品、活动规则的信息吸收程度，避免信息过载或内容过于简单，提升转化效率

  - 做多轮对话类Agent的AB测评估时，可复用KnowSim的3个量化指标（KG/DC/CO），替代单一的LLM judge评分，提升评估结果和真实用户体验的对齐度

  - 针对不同分层用户（如新客/熟客、下沉市场/一二线用户）做内容推送、话术生成时，不要用通用聚合排名选模型，要针对目标用户群单独做benchmark'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM用户模拟器无显式的用户动态知识状态建模，既无法模拟不同知识水平用户的真实交互行为，也无法量化LLM的信息校准能力（即输出内容匹配用户当前认知水平、认知容量的能力），导致评估结果和真实用户体验对齐度低，也无法解释效果差异的底层原因。

### 方法关键点
- 为每个问题构建Information Unit（IU）有向无环图：节点为独立知识单元，边为知识前置依赖关系，全量覆盖理解问题所需的所有概念
- 模拟器维护用户动态知识状态：每个IU的掌握程度分为unaware/struggling/partial/knows_well四档，每轮交互后基于学习理论规则更新状态，同时引入认知过载限制吸收效率
- 输出三个可解释的量化指标：Knowledge Gain（用户知识增量）、Delivery Calibration（信息传递校准度）、Cognitive Overload（认知过载程度），无需额外LLM判分
- 对话终止基于知识掌握进度触发，而非固定轮数，更贴近真实用户交互逻辑

### 关键结果
- 跨数学解题、专业QA两个领域构建KNOWCHAT数据集，包含705段按用户知识水平分层的人机会话
- 和3个基线用户模拟器对比，KnowSim与人类判断的符号一致性达73-74%（p=0.003），显著优于所有基线
- 测试9款主流LLM，发现最优模型随用户知识水平存在明显排名反转：DeepSeek V4对新手用户知识增益最高，Gemini 3.1 Pro更适配进阶用户，这类差异在传统聚合评估榜单中完全不可见

### 最值得记住的话
针对不同知识水平的用户群体，LLM的信息校准表现存在完全的排名反转，仅依赖聚合榜单选型会系统性损害特定用户群的体验。
