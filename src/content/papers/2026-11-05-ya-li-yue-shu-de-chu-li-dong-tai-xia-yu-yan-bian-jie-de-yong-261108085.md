---
title: Linguistic boundaries emerge from pressure-constrained processing dynamics
title_zh: 压力约束的处理动态下语言边界的涌现机制研究
authors:
- Rui He
- Philipp Homan
- Wolfram Hinzen
affiliations:
- Universitat Pompeu Fabra
- University of Zurich
- ETH Zurich
- Institució Catalana de Recerca i Estudis Avançats
arxiv_id: '2611.08085'
url: https://arxiv.org/abs/2611.08085
pdf_url: https://arxiv.org/pdf/2611.08085
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 语言认知动力学 · LLM表征特性
tags:
- Linguistic_Boundary
- Cognitive_Dynamics
- LLM_Representation
- Reading_Time
- Natural_Language_Processing
one_liner: 揭示语言边界从三类处理压力动态交互中自发涌现的认知与计算规律
practical_value: '- 大模型长文本推理场景中，可参考边界检测逻辑（未解决依赖下降、整合成本峰值）触发KV cache分段重置，降低内存开销

  - 生成式推荐/Agent多轮会话场景中，可基于语义整合成本、依赖负载变化自动识别对话意图边界，优化上下文窗口裁剪策略

  - 电商文案/广告创意优化场景中，可利用边界涌现规律调整句子长度与结构，降低用户阅读认知负荷，提升点击率转化率'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
人类认知会将连续的语言输入拆分为词、短语、句子等带边界的结构单元，但这类边界的自发涌现机制缺乏统一解释，也未验证LLM的文本处理过程是否存在同类规律。
### 方法关键点
1. 构建无预定义边界、无成分标签的生成模拟，验证未解决依赖维持、已完成关系整合、语义上下文更新三类压力的交互可触发边界涌现
2. 结合人类听力边界标注实验、自然场景自步阅读实验交叉验证规律
3. 测试LLM处理自然叙事时的隐层表征变化与语言边界的关联
### 关键结果
人类边界选择预测效果显著优于句法、韵律特征基线；LLM句子结尾处局部本征维度提升，隐状态轨迹更平直，后续表征更新幅度更大；边界可解释10%以上的阅读时间变异，但对next-token surprisal的解释力不足5%
