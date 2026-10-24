---
title: 'OP-Print: Tracing Membership Imprints in On-Policy Self-Distillation'
title_zh: OP-Print：追踪同策略自蒸馏中的训练样本成员印记
authors:
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.31616'
url: https://arxiv.org/abs/2610.31616
pdf_url: https://arxiv.org/pdf/2610.31616
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 模型隐私 · 同策略自蒸馏成员推理攻击
tags:
- membership inference attack
- on-policy distillation
- self-distillation
- gray-box attack
- black-box attack
- privacy risk
one_liner: 首个面向同策略自蒸馏的成员推理攻击框架，覆盖灰盒黑盒场景且效果远超基线
practical_value: '- 针对采用自蒸馏优化的推荐/Agent业务模型，可复用OP-Print的检测逻辑做隐私合规自查，规避训练样本泄露风险

  - 若业务模型需对抗成员推理攻击，可针对性打散不确定性敏感位点的修正印记，降低可被攻击的特征辨识度

  - 黑盒场景下的输出稳定性度量方法可复用为模型训练数据泄露风险的无侵入检测工具'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
on-policy self-distillation因无额外教师依赖、分布偏移小被广泛用于模型性能优化，但该范式的隐私风险长期未被探明，同一样本的双视角输入会强化模型记忆，存在训练样本成员泄露隐患。
### 方法关键点
1. 核心发现：on-policy self-distillation的监督印记呈稀疏结构化特征，仅集中在不确定性敏感的修正位点，而非覆盖全输出序列
2. 灰盒攻击：直接聚合同输出序列下的师生残差修正量作为攻击特征
3. 黑盒攻击：用多次重启推理的输出 basin 稳定性作为隐式修正过程的可观测代理
### 关键结果
在多模型、多蒸馏方案的测试集上，所有基线攻击准确率仅接近随机猜测水平，OP-Print在灰盒、黑盒两种权限下均被验证具备有效攻击能力。
