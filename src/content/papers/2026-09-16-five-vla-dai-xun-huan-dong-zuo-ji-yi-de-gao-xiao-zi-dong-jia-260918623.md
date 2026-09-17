---
title: 'FIVE-VLA: Fast and EffectIVE Autonomous Driving with Recurrent Action Memory'
title_zh: FIVE-VLA：带循环动作记忆的高效自动驾驶视觉语言动作模型
authors:
- Kemal Oksuz
- Alexandru Buburuzan
- Yuhan Yao
- Puneet K. Dokania
affiliations:
- Robert Bosch GmbH, Germany
- Five AI Ltd., United Kingdom
arxiv_id: '2609.18623'
url: https://arxiv.org/abs/2609.18623
pdf_url: https://arxiv.org/pdf/2609.18623
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 自动驾驶 · 轻量VLA推理优化
tags:
- VLA
- Autonomous Driving
- Efficient Encoder
- Temporal Memory
- Edge Inference
one_liner: 提出641M参数轻量FIVE-VLA，搭配高效视觉编码器与循环动作记忆，实现自动驾驶效果与推理速度双提升
practical_value: '- 多模态系统降本：高效视觉编码器的token压缩思路可迁移到多模态推荐的图像编码器优化，减少高分辨率物料的token数量，降低推理延迟

  - 时序记忆模块复用：Recurrent Action Memory（RAM）的轻量时序上下文建模思路，可用于推荐系统用户行为序列建模、Agent历史交互记忆模块设计，无需扩容大模型参数即可提升时序决策一致性

  - 推理链路剪枝：跳过不必要文本生成直接输出目标结果的思路，可用于Agent决策、生成式推荐的推理链路优化，砍掉无用自回归生成步骤，大幅降低时延'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前自动驾驶领域SOTA VLA存在参数量过大、高分辨率图像处理效率低、缺失时序记忆三大核心问题，难以适配车载边缘设备的低延迟要求。
### 方法关键点
1. 采用高效视觉编码器，处理448×896高分辨率图像仅生成98个token，比现有方案少5倍以上，同时跳过文本生成环节直接单步输出轨迹预测结果；
2. 新增轻量Recurrent Action Memory（RAM）模块，基于历史动作token做动作预测，为超车、紧急制动等场景提供时序上下文支撑。
### 关键结果
仅641M参数量，在Bench2Drive闭环benchmark上无违章路线完成率比之前SOTA高~10%；在NVIDIA Physical AI AV数据集上，单/四视角下碰撞违规率比SimLingo低10.2%/7.7%；推理速度在A100达~30fps、T4达~4fps，比之前方案提速8~30倍。
