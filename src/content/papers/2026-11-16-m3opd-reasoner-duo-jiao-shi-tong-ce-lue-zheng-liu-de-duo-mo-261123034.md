---
title: 'M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with
  Multi-Teacher On-Policy Distillation'
title_zh: M3OPD-Reasoner：多教师同策略蒸馏的多模态推理训练开源方案
authors:
- Nguyen Quang Trung
- Hoang Phan
- Shuo Sun
- Longyin Zhang
- AiTi Aw
affiliations:
- A*STAR
- VinUniversity
arxiv_id: '2611.23034'
url: https://arxiv.org/abs/2611.23034
pdf_url: https://arxiv.org/pdf/2611.23034
published: '2026-11-16'
collected: '2026-11-18'
category: Training
direction: 多模态大模型 · 蒸馏训练方案
tags:
- Multimodal Reasoning
- On-Policy Distillation
- Reinforcement Learning
- Vision-Language Model
- Post-Training
one_liner: 提出多教师同策略蒸馏结合混合RL的多模态推理训练方案，开源全链路数据代码与权重
practical_value: '- 多技能融合训练可复用：电商多模态导购/商品理解Agent可先训练单域（商品属性识别/单据OCR/短视频理解）专家模型，再用MOPD蒸馏为单一模型，避免混合训练的能力冲突，降低部署成本

  - 数据复用技巧可借鉴：蒸馏完成的模型可复用同一批RL数据做二次强化训练，无需新增标注数据就能进一步提升效果，且无能力坍缩，适合业务数据有限的场景

  - SFT数据选择规则可复用：优先用学生模型自身生成的trace做SFT，比大模型生成的trace兼容性更好，图像类任务效果提升更明显，视频类任务可酌情用大模型trace

  - 奖励函数设计可直接复用：`R=0.9*准确率+0.1*格式分`的奖励规则适合带结构化输出要求的多模态任务（如商品属性抽取、用户需求结构化解析），同时保证结果正确和格式合规'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态推理模型训练普遍采用混合域SFT+RL方案，存在不同领域能力冲突、此消彼长的问题；已有的多教师蒸馏方案仅覆盖图像域，且蒸馏后缺乏复用RL数据进一步提升的相关研究，缺少覆盖图像STEM、图像感知、视频三域的全开源训练pipeline。
### 方法关键点
- 数据：构建1.35M规模的SFT数据集M3OPD-SFT-1.35M、193K带可验证奖励的RL数据集M3OPD-RL-193K，覆盖三个推理域，全部完成去重与基准测试集去污染。
- 三阶段训练pipeline：第一阶段针对每个域用GSPO训练单域教师模型（对比了有无SFT预热的效果）；第二阶段通过多教师同策略蒸馏（MOPD）将三个教师的能力迁移到同一学生模型；第三阶段复用同一批RL数据对蒸馏后的学生做MixRL训练，进一步挖掘数据价值。
- 奖励设计：RL阶段统一采用`R=0.9*Racc + 0.1*Rfmt`的规则奖励，只有格式校验通过的响应才计算准确率分，同时保证结果正确性和输出格式合规。
### 关键结果
- 以Qwen3.5-9B为base，MOPD蒸馏后的学生模型平均准确率达75.2%，比混合训练MixRL基线高0.8pct，与三个单域教师的平均效果持平；无SFT预热的教师蒸馏效果比带SFT预热的方案高1pct。
- 叠加MixRL后的最终模型M3OPD-Reasoner-9B平均准确率达75.9%，比base模型提升6.5pct，在21个测试基准中绝大多数达到SOTA或次SOTA水平，无明显能力短板。

最值得记住的结论：多教师同策略蒸馏和混合RL可作为前后衔接的训练阶段，在同一批数据上先后使用，既能高效融合多域能力，又能进一步提升效果，无需额外标注数据。
