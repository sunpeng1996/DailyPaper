---
title: 'World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot
  Manipulation'
title_zh: World-to-Wrist：面向细粒度机器人操作的任务条件未来腕部建模
authors:
- Yuhao Pan
- Haosong Peng
- Zhengshen Zhang
- Zhengyang Yan
- Yalun Dai
- Fushuo Huo
- Chujie Wang
- Tianyu Qi
- Xiucheng Wang
- Nan Cheng
affiliations:
- The Hong Kong University of Science and Technology
- National University of Singapore
- Nanyang Technological University
- Wuhan University
- Sun Yat-sen University
arxiv_id: '2608.05369'
url: https://arxiv.org/abs/2608.05369
pdf_url: https://arxiv.org/pdf/2608.05369
published: '2026-08-04'
collected: '2026-08-08'
category: Other
direction: 机器人操作 · 视觉语言动作模型
tags:
- VLA
- Robot Manipulation
- Vision-Language
- Latent Token
- Future Prediction
one_liner: 提出W2-VLA模型与W2-CoT标注流水线，提升多场景下机器人细粒度操作的实时性能
practical_value: '- 多模态输入差异化建模思路可迁移至多模态推荐：不同来源特征（如用户行为/商品图文/搜索query）无需直接平行拼接，可通过隐层token做中间接口适配不同分支预测需求

  - W2-CoT结构化辅助标注流水线设计思路可复用：针对复杂任务生成过程类监督信号，可降低大模型落地时的标注成本

  - 低延迟推理优化方案可参考：引入额外预测分支的同时保持80Hz以上生成速率，适合实时交互类Agent（如直播数字人、客服Agent）部署'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉语言动作（VLA）模型将主视角与腕部视角观测视为平行输入，忽略两类信息的角色差异，无法利用全局任务上下文预判腕部局部交互的演化，制约细粒度操作性能。
### 方法关键点
1. 提出W2-VLA模型，引入任务条件的隐式建模token作为VLM与腕部预测器的紧凑接口；
2. 腕部预测器基于接口与历史腕部观测预测未来腕部隐向量，转换为未来感知上下文支撑动作预测；
3. 配套W2-CoT合成流水线生成操作进度、物理转换提示、腕部局部证据三类结构化标注，为隐式接口提供辅助监督。
### 关键结果
在LIBERO、RoboTwin 2.0及真实操作任务上，单臂/双臂场景下细粒度、接触敏感操作性能均有提升，动作生成速率保持80Hz以上。
