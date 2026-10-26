---
title: 'SliderEdit++: Improved Slider Trajectories in Instruction-Based Image Editing'
title_zh: SliderEdit++：面向指令式图像编辑的滑块轨迹优化方法
authors:
- Arman Zarei
- Sayan Nag
- Bryan Wang
- Franck Dernoncourt
- Varun Manjunatha
- Nedim Lipka
- Soheil Feizi
- Samyadeep Basu
affiliations:
- Adobe Research
- University of Maryland
arxiv_id: '2610.14253'
url: https://arxiv.org/abs/2610.14253
pdf_url: https://arxiv.org/pdf/2610.14253
published: '2026-10-13'
collected: '2026-10-26'
category: Other
direction: 指令式图像编辑 · 连续可控交互
tags:
- Image Editing
- Controllable Generation
- Interactive AI
- Benchmark
- Trajectory Regularization
one_liner: 提出图像连续编辑基准SlideBench与轨迹正则化方法SliderEdit++，提升可控性同时提速3-20倍
practical_value: '- 电商商品图智能修图类交互产品可借鉴轨迹正则化思路，优化滑动条调节效果，避免修图强度调整时出现视觉跳变，提升用户操作体验

  - 多调节控件的解耦目标函数可迁移至多参数联合控制场景（如同时调整商品图亮度/饱和度/滤镜强度），避免不同调节参数互相干扰

  - 少步推理骨干网络的选型思路可复用在低延迟要求的交互类AI功能的工程优化中，有效降低功能响应时延'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令驱动图像编辑的滑块连续控制能力不可靠，滑动时易出现视觉跳变、非单调变化，多滑块共同控制时存在相互干扰，且缺乏统一评测基准。

### 方法关键点
1. 构建SlideBench基准，覆盖多类编辑场景，配套单调性、感知连续性、滑块间解耦度三类统一评测指标；
2. 提出SliderEdit++，放弃仅端点监督的范式，新增速度域、语义空间的中间编辑轨迹正则化+谱控制，保障滑块滑动过程平滑可预测；
3. 加入解耦目标降低多个独立编辑控件的相互干扰，采用少步编辑骨干网络降低推理延迟。

### 关键结果
在SlideBench上相较最优基线整体得分相对提升18.5%，推理速度是现有滑块编辑方法的3~20倍，大幅提升交互响应性
