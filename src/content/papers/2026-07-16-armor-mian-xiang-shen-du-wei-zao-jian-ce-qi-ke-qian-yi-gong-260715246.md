---
title: 'ARMOR++: Agentic Orchestration of a Multi-Domain Primitive Set for Transferable
  Attacks on Deepfake Detectors'
title_zh: ARMOR++：面向深度伪造检测器可迁移攻击的多智能体编排框架
authors:
- Christos Korgialas
- Gabriel Lee Jun Rong
- Dion Jia Xu Ho
- Pai Chet Ng
- Xiaoxiao Miao
- Konstantinos N. Plataniotis
affiliations:
- 亚里士多德大学塞萨洛尼基分校
- 新加坡理工学院
- 哥伦比亚大学
- 昆山杜克大学
- 多伦多大学
arxiv_id: '2607.15246'
url: https://arxiv.org/abs/2607.15246
pdf_url: https://arxiv.org/pdf/2607.15246
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: 多智能体编排 · 黑盒对抗攻击
tags:
- Multi-Agent
- Adversarial Attack
- Deepfake Detection
- VLM
- Black-box Attack
- Transferability
one_liner: 结合VLM语义先验与LLM调度，构建多Agent多域扰动框架，大幅提升深度伪造检测器无查询黑盒攻击迁移率
practical_value: '- 多Agent分层架构可直接复用：做复杂业务任务（多策略召回融合、跨域广告投放优化）时，可拆分感知Agent（语义分析）、执行Agent（策略落地）、调度Agent（超参调优）、融合Agent（结果合并）的分层解耦架构，降低复杂系统迭代成本

  - 熵正则化多候选融合技巧可落地：多模型/多策略输出融合时，加入熵正则项鼓励策略多样性，再动态退火平衡探索-利用，比简单加权/投票的跨场景泛化性更好，可直接用于多召回源排序融合、多AB实验策略合并场景

  - 无查询自适应调优框架可借鉴：需要在无目标侧反馈的场景（跨域推荐冷启动、第三方广告平台投放）做策略迭代时，可参考代理指标+停滞检测自动放宽约束的机制，减少对目标侧回流数据的依赖'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有深度伪造检测器的黑盒迁移攻击存在明显短板：跨架构（CNN代理模型到Transformer目标模型）迁移成功率极低，严格无查询约束下扰动空间单一容易过拟合代理模型，此前的Agent攻击方案仅支持空间域扰动、依赖黑盒反馈项，泛化性不足。

### 方法关键点
- 多Agent分层架构：感知层用Qwen2.5-VL生成空间语义先验掩码，加权扰动梯度；调度层分别负责初始化约束、自适应调优各扰动原语超参、检测优化停滞自动放宽扰动预算/质量约束；执行层并行运行5种多域扰动原语（优化类CW、显著性类JSMA、空间变换类STA、频域类SSA、块结构类BSR），覆盖不同模型的归纳偏置；融合层用熵正则化加权融合算法合并多原语扰动
- 全程严格遵循无查询协议：仅在最终生成对抗样本后查询一次目标检测器做评估，所有优化、调参、融合全靠3个CNN代理模型的反馈

### 关键结果
在AADD-2025低/高质量两个子集、DFDC-Preview零样本数据集上测试，目标为ViT-B/16、Swin-B两个Transformer深度伪造检测器，对比12个baseline：AADD-LQ子集上ARMOR++盲目标攻击成功率（ASR）达44.3%（ViT-B/16）、40.8%（Swin-B），比最优Agent baseline ARMOR分别高4.7、3.7个百分点，比非Agent最优AA-PGD高24.7、22.5个百分点；AADD-HQ子集上ASR达32.1%（ViT-B/16）、28.7%（Swin-B），同样领先所有baseline，且感知质量与ARMOR基本持平。

**最值得记住的结论**：多域能力覆盖+Agent自适应编排，是提升黑盒场景下策略跨分布迁移性的有效路径，比单一策略暴力优化的投入产出比更高。
