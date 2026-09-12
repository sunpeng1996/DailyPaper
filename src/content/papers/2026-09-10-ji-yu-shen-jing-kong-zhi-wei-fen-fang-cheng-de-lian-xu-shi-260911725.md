---
title: Continuous-Time Acoustic Modelling with Neural Controlled Differential Equations
title_zh: 基于神经控制微分方程的连续时间声学建模
authors:
- Mattias Cross
- Minghui Zhao
- Anton Ragni
affiliations:
- University of Sheffield
- Speech and Hearing Group, University of Sheffield
arxiv_id: '2609.11725'
url: https://arxiv.org/abs/2609.11725
pdf_url: https://arxiv.org/pdf/2609.11725
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 语音合成 · 连续时间声学建模
tags:
- TTS
- Neural CDE
- Acoustic Modelling
- Emotional Speech
- Continuous-Time Model
one_liner: 引入神经控制微分方程实现TTS时长感知连续声学建模，提升合成语音情感强度排序匹配度
practical_value: '- 电商智能客服、直播数字人语音合成场景可引入Neural CDE做时长感知建模，提升情感表达与真实场景的匹配度

  - 情感化语音生成业务中可通过调整采样步长平衡风格跟踪精度与绝对校准效果，适配不同交互场景需求

  - 连续时间轨迹建模思路可迁移到推荐系统用户兴趣建模，刻画用户行为序列在时间维度上的动态演化'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有TTS系统通过预测时长将音素级编码态扩展为帧级解码输入的对齐方案，仅调整隐态的出现位置与频次，不改变隐态本身取值，难以支撑时长相关的风格、情感等细粒度表达需求。
### 方法关键点
将音素表征构建为时间参数化控制路径，通过神经声学向量场生成连续时间隐状态，其取值随音素内容和时长衍生的时序信息动态演化；生成的连续轨迹可离散采样后直接接入标准声学解码器pipeline。
### 关键结果
主观测试显示单步处理1个音素的CDE模型，合成语音与参考语音的情感强度排序一致性显著提升，同时情感表达质量与强基线相当；半音素步长实验表明，时间分辨率可调节风格跟踪与绝对校准的权衡关系。
