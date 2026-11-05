---
title: From Pixels to Actions - Towards Native Vision-Language-Action Policies
title_zh: 从像素到动作：原生视觉-语言-动作策略框架研究
authors:
- Weichen Fan
- Haiwen Diao
- Penghao Wu
- Siyuan Hu
- Ziqi Huang
- Tianqi Liu
- Mingze Sun
- Ziyi Wang
- Zhongang Cai
- Hanming Deng
affiliations:
- S-Lab, Nanyang Technological University
- SenseTime Research
- Ropedia
arxiv_id: '2611.06918'
url: https://arxiv.org/abs/2611.06918
pdf_url: https://arxiv.org/pdf/2611.06918
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: 具身Agent · 视觉-语言-动作策略优化
tags:
- VLA
- Embodied Agent
- Vision Representation
- Action Policy
- Multimodal Fusion
one_liner: 提出无视觉编码器的NEO-VLA框架，通过多层级视觉表征提升具身Agent控制性能与鲁棒性
practical_value: '- 开发电商多模态导购Agent、商品细粒度识别模型时，可放弃仅用预训练视觉编码器最终输出的做法，融合中浅层视觉特征，减少局部纹理、尺寸、姿态等关键信息丢失，提升识别准确率

  - 多模态融合架构设计可参考视觉、语言token在backbone全程联合演进的思路，替代先独立编码再跨模态对齐的传统方案，降低信息压缩带来的性能损耗

  - 分布偏移场景（如用户实拍商品图检索、不同光照下的直播内容理解）的多模态任务，可引入多层级表征融合机制，有效提升模型鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型默认先通过独立视觉编码器压缩视觉信息，再开展动作推理，会丢失局部几何、边界、深度、细微状态变化等对决策关键的细粒度视觉信号，分布偏移下性能衰减严重。
### 方法关键点
无独立视觉编码器的NEO-VLA框架采用轻量patch卷积层做图像token化，视觉token与语言token在 backbone 全程联合演进，flow-matching动作专家可调用不同深度的指令对齐视觉表征做决策。
### 关键结果
相同控制条件下原生架构性能优于编码器基准，全微调后性能差距仍然存在，单纯扩大模型规模无法弥补该差距；层探针实验显示动作关键信号往往在视觉表征中浅层就达到峰值；多操作场景、分布偏移下控制性能与鲁棒性显著优于基线。
