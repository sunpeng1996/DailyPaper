---
title: 'PixelEyes: Decoupling Perception and Reasoning for Pinpoint Visual Evidence
  Seeking'
title_zh: PixelEyes：解耦感知与推理的精准视觉证据查找多轮Agent
authors:
- Dengxian Gong
- Yuanzheng Wu
- Haobo Yuan
- Zhengdong Hu
- Tao Zhang
- Yikang Zhou
- Shihao Chen
- Quanzhu Niu
- Kai Wang
- Jason Li
affiliations:
- Wuhan University
- UC Merced
- UTS
- NUS
- NTU
arxiv_id: '2607.00115'
url: https://arxiv.org/abs/2607.00115
pdf_url: https://arxiv.org/pdf/2607.00115
published: '2026-06-29'
collected: '2026-07-03'
category: Agent
direction: 多模态视觉Agent · 感知推理解耦
tags:
- Multi-modal Agent
- Visual Reasoning
- Decoupled Architecture
- SAMTok
- BFS Search
- Active Perception
one_liner: 解耦感知与推理，结合mask引导裁剪与语义区域BFS，实现SOTA多轮视觉证据查找
practical_value: '- 电商商品细粒度检索/合规审核场景，可直接复用mask引导的解耦感知架构，外接SAM类分割工具，无需联合训练感知能力，降低训练成本同时提升小目标定位精度

  - 多轮交互类Agent（如电商导购Agent）的探索策略设计，可借鉴Semantic-Region BFS思路，锚定全局坐标+记录已探索语义区域，避免DFS导致的局部循环，大幅减少交互轮数

  - 多模态Agent训练可复用专家轨迹合成思路：用强基座+工具增强生成高质量交互轨迹做SFT，再用GRPO优化路径效率，效果远优于盲目扩充训练数据量

  - 广告/推荐场景高分辨率素材质检（如主图小字合规、logo检测），可复用Pinpoint-Bench的评估体系，用LSR、TAE指标拆分定位/推理失败，精准定位模型瓶颈'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多轮视觉推理Agent将感知与推理耦合在单个MLLM中，存在两个核心缺陷：一是MLLM的定位精度远低于专用感知模型，错误裁剪会产生大量冗余交互轮次；二是带背景噪声的粗裁剪易引发「注意盲视」，即使定位到目标区域也无法正确识别，在目标占比不足0.1%的超高分辨率图上表现尤其差。

### 方法关键点
- 架构解耦：通用VLM负责高层推理，决策「找什么」；外接专用分割模型SAMTok作为感知工具，输出像素级mask定位目标，裁剪时过滤背景噪声
- 搜索策略：采用语义区域BFS，所有坐标锚定原始全局图，记录已探索语义区域，感知工具返回空mask时直接切换到未探索区域，避免局部循环
- 可切换工具：实例定位优先用mask裁剪，图表/密集文本等无明确实例的场景自动回退到bbox裁剪，兼顾精度和通用性
- 训练数据：用Gemini-3-Flash增强SAMTok工具，合成5.8K符合架构逻辑的高质量专家轨迹（PixelEyes-6K），先SFT再用GRPO强化学习优化路径效率
- 评估基准：发布Pinpoint-Bench，包含433个零提示超高分辨率样本，目标平均占比仅0.07%，提供LSR（定位成功率）、TAE（轮次效率）指标，可拆分定位与推理失败

### 关键实验
在V*、HR-Bench、VisualProbe、Pinpoint-Bench等6个基准上全面领先现有SOTA：4B参数版本比基线Qwen-3-VL-4B在V*上提升11.52%，在Pinpoint-Bench上准确率达54.73%，平均仅需2.09轮，TAE是Mini-o3的3倍以上；8B版本准确率达55.20%，甚至超过235B参数的Qwen-3-VL在V*等基准上的表现。

最值得记住的结论：视觉推理Agent的性能提升核心是优化搜索结构与逻辑，而非盲目增加交互轮次或模型参数。
