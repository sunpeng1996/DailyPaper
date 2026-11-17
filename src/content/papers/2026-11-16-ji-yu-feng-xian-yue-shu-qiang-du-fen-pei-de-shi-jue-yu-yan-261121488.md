---
title: Detection-Efficient Watermarking for Vision--Language Agents via Risk-Constrained
  Strength Allocation
title_zh: 基于风险约束强度分配的视觉语言Agent高效检测水印方法
authors:
- Dumindu Samaraweera
- Prashant Shekhar
affiliations:
- Embry-Riddle Aeronautical University, USA
arxiv_id: '2611.21488'
url: https://arxiv.org/abs/2611.21488
pdf_url: https://arxiv.org/pdf/2611.21488
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 多模态Agent · 可信水印自适应分配
tags:
- Vision-Language Agent
- Watermarking
- Adaptive Allocation
- Content Provenance
- Trustworthy AI
one_liner: 提出融合预测不确定性和多模态风险代理的自适应水印策略，优化检测与质量的trade-off
practical_value: '- 电商多模态商品生成、导购Agent输出的水印可直接复用该分配逻辑：对商品属性、优惠信息、履约规则等语义关键token降低水印强度，避免生成错误；对风格描述、承接话术等非关键token提升水印强度，平衡溯源能力和生成质量

  - 单参数λ调节trade-off的架构设计可直接复用，业务上线无需重训模型，只需在业务真实流量上扫λ即可快速匹配场景要求的溯源准确率/用户体验平衡点，大幅降低落地成本

  - 水印阈值校准必须重视小样本漂移问题，电商场景需定期用真实未水印的用户query、生成内容重校准阈值，避免误判合规内容为非授权生成内容，引发运营风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有视觉语言Agent（VLA）输出已广泛用于多模态导购、商品描述生成、合规审核等场景，需要水印机制实现内容溯源、授权校验和事后审计，但固定强度水印会无差别修改语义关键token（如商品属性、视觉特征、决策指令），严重降低输出质量和可用性；现有自适应水印方案仅基于生成不确定性分配强度，未考虑多模态输入的语义相关性，且无法区分增益来自更低的总干预强度还是分配策略本身。
### 方法关键点
- 融合两类信号做token级水印强度分配：一是归一化的生成分布熵（衡量模型改词自由度，越高越适合加水印），二是零样本多模态相关风险代理（融合语言上下文、局部显著性、图像特征与候选token的余弦相似度，衡量当前token语义重要性，越高越不适合加水印）；
- 基于风险惩罚系数λ构建局部优化目标，推导闭形式强度分配规则，仅调整λ即可连续调节检测准确率与输出质量的平衡点，无需修改模型、检测器或重新训练；
- 提出匹配强度分析方法，隔离总水印预算和分配策略的效果，准确衡量策略的检测效率。
### 关键实验
在AMBER基准1000个图像-query实例上测试，基于LLaVA-1.5-7B模型，对比固定强度、仅熵驱动、仅关键度驱动三类基线：
- 最优配置下相比固定强度水印，平均水印强度降低59.4%，困惑度变化从0.3634降至0.1689，干净/改写后样本ROC-AUC达0.9552/0.9459；
- 匹配相同平均水印强度时，该策略ROC-AUC比三类基线高约10个百分点，证明增益来自分配策略而非更低的干预强度；
- 小样本校准阈值会导致FPR漂移达1.82个百分点，必须报告校准方差作为可审计溯源系统的标准输出项。
> 最值得记住的一句话：自适应水印的核心价值不是全局最优，而是给业务提供可灵活调节的检测-质量连续前沿，匹配不同场景的合规和体验要求
