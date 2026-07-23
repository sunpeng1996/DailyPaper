---
title: Generalizable VLA Finetuning via Representation Anchoring and Language-Action
  Alignment
title_zh: 基于表征锚定与语言-动作对齐的可泛化视觉语言动作模型微调
authors:
- Dwip Dalal
- Shivansh Patel
- Chahit Jain
- Jeonghwan Kim
- Utkarsh Mishra
- Alex Baratian
- Hyeonjeong Ha
- Heng Ji
- Svetlana Lazebnik
- Unnat Jain
affiliations:
- University of Illinois Urbana-Champaign
- Texas A&M University
- University of California, Irvine
arxiv_id: '2607.13429'
url: https://arxiv.org/abs/2607.13429
pdf_url: https://arxiv.org/pdf/2607.13429
published: '2026-07-14'
collected: '2026-07-23'
category: Training
direction: 多模态大模型微调 · 表征对齐
tags:
- VLM
- Fine-tuning
- Representation Alignment
- Catastrophic Forgetting
- OOD Generalization
one_liner: 提出Anchor-Align双目标微调框架，缓解VLA微调表征漂移与模态错位，提升跨场景泛化性能
practical_value: '- 做多模态模型（如商品理解、多模态Agent）微调时，可借鉴层间表征蒸馏锚定思路，用冻结预训练模型做监督，缓解灾难性遗忘，保留预训练泛化能力

  - 做语义指令到落地动作/结果的映射任务时，可借鉴同观测下联合训练语义预测和目标输出的对齐思路，解决不同模态损失训练数据错位问题

  - 做OOD场景泛化优化时，可参考将连续目标转为离散语义标签的方式，降低跨模态对齐难度，提升鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练VLM微调为VLA时，行为克隆（BC）任务会逐步覆盖预训练表征，损伤原有视觉、语义泛化能力；现有图文数据共训练的优化方案未解决语言、动作损失在不同观测上训练导致的模态错位问题，潜在泛化缺陷无法被标准基准检出。
### 方法关键点
提出Anchor-Align微调框架，在BC损失基础上新增两个训练目标：
1. 视觉-语言锚定：从冻结的预训练VLM副本逐层蒸馏表征，避免微调过程中表征漂移
2. 语言-动作对齐：将连续动作目标转换为离散运动方向标签，在同一观测样本上联合训练语言预测、动作预测任务
### 关键结果
- 物理xArm7机器人测试中，两款主流VLA架构的真实任务成功率分别从28%提升至54%、37%提升至60%
- 仿真环境下，在LIBERO-PRO、LIBERO-Plus、CALVIN基准上，OOD扰动鲁棒性、感知鲁棒性、长时序控制性能均实现稳定提升
