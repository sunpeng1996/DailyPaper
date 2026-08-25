---
title: 'The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams'
title_zh: 多Agent团队的交互税：全方案通信会抹杀模型多样性增益
authors:
- Summer Eunhyung Ann
- Haokun Liu
- Chenhao Tan
affiliations:
- Department of Computer Science, University of Chicago
arxiv_id: '2608.23541'
url: https://arxiv.org/abs/2608.23541
pdf_url: https://arxiv.org/pdf/2608.23541
published: '2026-08-24'
collected: '2026-08-25'
category: MultiAgent
direction: 多Agent协作机制优化
tags:
- MultiAgent
- Diversity
- Communication Tax
- MoA
- LLM Collaboration
one_liner: 发现多Agent全方案通信的交互税效应，验证独立生成+定向critique可规避多样性损失
practical_value: '- 搭建多Agent工作流时优先采用MoA类架构：先让不同基座独立生成候选方案，再统一选择/合成，避免Agent过早互相读取完整输出导致多样性坍塌，适合营销文案生成、多策略召回融合等场景

  - 仅当任务的约束可被LLM精确定位和修复时（比如优惠券发放规则校验、广告文案合规检查），才引入critique交互环节，否则优先用独立采样选优，降低不必要的交互成本

  - 多Agent选型优先选能力互补的基座，而非同基座多实例：同基座交互可小幅提升效果，异基座全量交互反而会损失多样性带来的增益，更适配复杂推荐策略优化、用户问题解决等场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多Agent LLM系统的效果存在矛盾结论：部分工作验证辩论、critique环路、MoA等架构能带来增益，另一部分则发现在同等预算下多Agent交互反而增加成本无效果提升。核心原因是缺乏对不同通信模式的差异分析，异质模型的多样性是多Agent系统的核心价值，但不合理的通信会抹除这种多样性。

### 方法关键点
- 覆盖11个带确定性验证器的优化任务，统一控制各工作流的计算资源预算，测试10种单/多Agent配置，包括单步生成、Best-of-N、自优化、Chain、MAgICoRe、Debate、HPE、MoA等
- 定义MEG（边际认知增益）衡量配置是否优于最优单Agent基线，MIG（边际交互增益）衡量交互是否优于同组Agent独立生成的效果
- 对比同基座多实例、异基座（Claude、GPT-4o、Gemini）多实例两类团队在不同通信模式下的表现

### 关键实验结果
- 异基座团队无交互时，任务最低Q分始终>0，而同基座团队至少有1个任务Q分为0，多样性带来的覆盖增益系数达+0.188（p<0.001）
- 全方案交互下，Chain、MAgICoRe、Debate三类架构在同基座团队MIG为正（+0.051、+0.044、+0.012），但异基座团队MIG转负（-0.024、-0.035、-0.078），多样性完全被抹除
- 仅MoA架构（生成阶段完全独立）的异基座MIG保持正值（从同基座+0.012提升到+0.016）；critique仅在错误易定位场景（如背包问题）下能提升可行性（从20%提升到100%），错误难定位场景反而降低效果

**最值得记住的结论**：多Agent的效果核心不取决于Agent数量，而取决于交换的信息类型和时机，全方案交互是最弱的默认选择。
