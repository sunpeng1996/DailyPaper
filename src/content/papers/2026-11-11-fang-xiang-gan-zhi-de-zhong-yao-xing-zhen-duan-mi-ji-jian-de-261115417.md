---
title: 'When Direction Matters: Diagnosing Relational Instruction Following in Dense
  Retrieval'
title_zh: 《方向感知的重要性：诊断密集检索的关系指令遵循能力》
authors:
- Zhanyu Wu
- Richong Zhang
affiliations:
- Beihang University
- Zhongguancun Laboratory
arxiv_id: '2611.15417'
url: https://arxiv.org/abs/2611.15417
pdf_url: https://arxiv.org/pdf/2611.15417
published: '2026-11-11'
collected: '2026-11-13'
category: RecSys
direction: 密集检索 · 指令遵循能力诊断
tags:
- Dense Retrieval
- Instruction Following
- Relational Reasoning
- Evaluation Dataset
- Zero-shot Retrieval
one_liner: 提出SwitchIR诊断集，揭示现有指令感知检索模型在关系方向反转任务上的严重性能缺陷
practical_value: '- 做电商商品/问答检索的指令感知召回时，可补充关系方向反转的硬负样本（如「A的参数」和「参数A对应的商品」、「买X送Y」和「买Y送X」这类歧义query）参与微调，避免语义匹配错误

  - 选型检索模型时，不要只看FollowIR等通用检索指标，要针对性测试关系方向类case的准确率，尤其是涉及因果、时序、比较类的用户高频query

  - 微调指令感知检索模型时，采用多关系类别的训练数据比单关系数据泛化性更强，且优先选择4B以上规模模型，跨关系泛化效果提升显著

  - RAG落地涉及定向关系查询（如「销量高于1000的商品」「退货率低于3%的品牌」）的场景，优先用4B以上跨编码器reranker做二次排序，方向识别准确率可提升20pct以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有指令感知密集检索模型在带显式属性、约束提示的任务上表现优异，但现有评测体系未覆盖仅反转关系方向、实体与词汇完全一致的场景，而电商、搜索场景中大量用户查询仅存在关系方向差异，这类硬错误会严重影响用户体验。
### 方法关键点
- 提出SwitchIR诊断数据集，包含受控模板集和人工校验的真实场景集，覆盖3类任务：Constraint Shift（带属性提示的控制组）、Explicit Filtering（仅交换包含/排除属性的控制组）、Relational Flip（仅反转关系方向的核心诊断组，覆盖因果、时序、比较、包含等6类常见关系）
- 设计4项递进评测指标：PairAcc（单条指令准确率）、FlipBoth（正反方向指令均正确的比例）、ParaAll（同义改写指令均正确的比例）、ContrastAll（正反方向+所有同义改写均正确的比例）
- 提出排序边际分解方法，将检索得分差拆解为方向无关的文档对固有偏好项和方向敏感的交互项，可准确定位模型失败原因
### 关键结果
- 零-shot评测覆盖10+主流检索模型：受控集上Constraint Shift的FlipBoth平均达0.986，Explicit Filtering的ContrastAll平均达0.923，而核心诊断项Relational Flip的ContrastAll仅0.015；真实场景集对应指标分别为0.943、0.679、0.084
- 4B规模跨编码器reranker在Relational Flip上表现最优，真实场景ContrastAll达0.47，仍存在53%的性能缺口
- 微调实验显示，多关系训练的4B embedding模型在未见过的关系类别上，受控集ContrastAll达92.5%，真实场景达70.1%，远优于0.6B模型的35.7%和13.5%
> 最值得记住的结论：现有指令感知检索模型在显式约束任务上的高性能不代表其具备可靠的关系角色绑定能力，关系方向类任务的核心瓶颈是方向敏感交互信号不足以覆盖方向无关的文档对固有偏好
