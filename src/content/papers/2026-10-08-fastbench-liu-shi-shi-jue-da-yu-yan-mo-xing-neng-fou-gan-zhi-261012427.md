---
title: 'FastBench: Can Streaming VLMs Perceive High-Dynamic Real-World Streams?'
title_zh: FastBench：流式视觉大语言模型能否感知高动态真实世界视频流？
authors:
- Yuxuan Hu
- Weikang Shi
- Yang Bo
- Xudong Lu
- Xintong Guo
- Shuhan Li
- Yuyang He
- Huankang Guan
- Peiwen Sun
- Yunqiao Yang
affiliations:
- CUHK MMLab
- Huawei Research
arxiv_id: '2610.12427'
url: https://arxiv.org/abs/2610.12427
pdf_url: https://arxiv.org/pdf/2610.12427
published: '2026-10-08'
collected: '2026-10-09'
category: Eval
direction: 流式VLM · 高动态场景评测
tags:
- Streaming VLM
- Benchmark
- High Dynamic Scene
- Frame Sampling
- Video Understanding
one_liner: 推出高动态流式VLM评测基准FastBench及免训练自适应帧率采样基线ProactiveFrame
practical_value: '- 电商直播、短视频多模态Agent可复用双层滑动窗口帧率调度策略：近期帧保留高帧率、历史帧降采样，在context预算有限时平衡时序精度与历史长度

  - 高动态短视频/直播内容理解场景，可优先测试24FPS采样策略，相比2FPS能提升近12%的VLM理解准确率，超过阈值后收益饱和无需继续扩容

  - 多模态内容审核、直播高光检测等快事件感知场景，可借鉴ProactiveFrame免训练自适应帧率调整思路，降低推理成本同时提升精度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有流式VLM评测基准多针对低动态场景，普遍采用1-2FPS稀疏采样会遗漏快事件，上下文预算约束下难以平衡时序历史、空间分辨率、时序粒度三者关系。

### 方法关键点
1. 构建轨迹驱动的FastBench评测集：从高FPS片段生成QA，过滤2FPS可回答问题，经SAM3、CoTracker3轨迹验证+三轮人工校验，得到覆盖8个领域、6类能力、3种时间范围的306个带证据区间的标注QA。
2. 提出免训练基线ProactiveFrame：通过文本token调整输入帧率，双层滑动窗口保留近期高FPS观测、旧帧降采样为稀疏历史。

### 关键结果
- 最强模型Gemini-3.5-Flash得分仅50.7%，高动态感知能力缺口显著
- Qwen3-VL-8B采样率从2FPS升至24FPS时，准确率从32.9%提升至44.6%，继续提帧率收益随历史压缩饱和
- ProactiveFrame较均匀稀疏采样分别提升5.4、1.5个百分点，但远低于oracle引导方案
