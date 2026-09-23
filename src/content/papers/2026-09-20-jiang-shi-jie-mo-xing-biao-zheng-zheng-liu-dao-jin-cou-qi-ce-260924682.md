---
title: 'Think Like a World Model, Act Like a VLA: Distilling World-Model Representations
  into Compact Robot Policies'
title_zh: 将世界模型表征蒸馏到紧凑Vision-Language-Action机器人控制策略
authors:
- Trung Dao
- Sankalp Yamsani
- Jaden Park
- Joohyung Kim
- Yong Jae Lee
arxiv_id: '2609.24682'
url: https://arxiv.org/abs/2609.24682
pdf_url: https://arxiv.org/pdf/2609.24682
published: '2026-09-20'
collected: '2026-09-23'
category: Training
direction: 知识蒸馏 · 大模型表征跨架构迁移
tags:
- Knowledge Distillation
- World Model
- VLA
- Representation Learning
- Efficient Inference
one_liner: 通过离线缓存世界模型特征的蒸馏方案，在不增加VLA推理成本的前提下提升鲁棒性
practical_value: '- 可复用离线缓存教师模型特征的蒸馏范式，训练阶段无需加载大尺寸教师模型，大幅降低大模型蒸馏的显存开销，适合生成式推荐、Agent小模型蒸馏场景

  - 仅蒸馏教师表征、舍弃生成/推理模块的思路，可将大模型的常识、环境感知能力迁移到小尺寸推荐/Agent模型，完全不增加部署后的推理成本

  - 轻量特征对齐训练目标的设计可复用在跨模型表征迁移任务中，适配不同学生模型的规模、骨干网络，泛用性强'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型仅做观测到动作的映射，无世界响应建模目标，鲁棒性受训练数据覆盖限制；世界模型具备场景感知能力，但单步决策延迟达秒级，无法嵌入实时控制链路。

### 方法关键点
将世界模型的场景认知能力与生成链路解耦，仅迁移其内部表征，舍弃生成模块；训练前离线运行冻结世界模型得到所有训练帧特征并缓存，训练阶段仅新增特征对齐损失让学生VLA匹配缓存特征，训练结束后丢弃对齐层，部署模型与基线完全一致，无额外推理开销。

### 关键结果
0.8B参数学生VLA在LIBERO数据集准确率达97.9%，RoboCasa-GR1人形操作任务准确率从48.2%提升至50.5%；单卡RTX 5090推理仅32ms、显存占用1.86GB；效果增益不受学生规模、骨干网络、对齐层、教师模型变化影响，泛用性强
