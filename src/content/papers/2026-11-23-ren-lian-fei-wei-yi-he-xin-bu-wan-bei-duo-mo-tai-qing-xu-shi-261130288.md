---
title: 'Face Is Not All You Need: MIME Benchmark for Incomplete Multimodal Emotion
  Recognition'
title_zh: 人脸非唯一核心：不完备多模态情绪识别基准MIME
authors:
- Yuxin Jia
- Xing Lan
- Wensong Wang
- Jian Xue
- Feiliang Ren
- Ke Lu
affiliations:
- School of Computer Science and Engineering, Northeastern University
- Hubei Key Laboratory of Multimedia and Network Communication Engineering, Wuhan
  University
- State Key Lab. of Novel Software Technology, Nanjing University
- National Engineering Research Centre for Multimedia Software (NERCMS), Wuhan University
- School of Engineering Science, University of Chinese Academy of Sciences
arxiv_id: '2611.30288'
url: https://arxiv.org/abs/2611.30288
pdf_url: https://arxiv.org/pdf/2611.30288
published: '2026-11-23'
collected: '2026-11-27'
category: Eval
direction: 多模态情绪识别 · 鲁棒性评测基准
tags:
- Multimodal Emotion Recognition
- MLLM
- Robustness
- Benchmark
- Chain of Emotion
one_liner: 定义不完备多模态情绪识别任务，构建MIME基准与CoE范式评测MLLM鲁棒性与推理过程
practical_value: '- 电商直播/短视频情绪分析场景不要仅依赖人脸特征，可补充肢体、场景特征作为人脸模糊/缺失时的补偿，提升识别鲁棒性

  - 多模态业务模型的鲁棒性评测可复用MIME的细粒度缺失设置，避免仅做全模态移除的粗粒度测试，更贴合真实业务噪声

  - 可借鉴CoE分析范式拆解MLLM从线索感知到推理的全链路，快速定位模型在特定业务场景下的性能瓶颈'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态情绪识别（MER）方案默认输入完备对齐、以人脸为核心推理锚点，真实场景下的模态退化、信息缺失会引发性能骤降，且当前缺少细粒度不完备场景下的系统性评测框架与可解释分析方法。
### 方法关键点
1. 正式定义不完备多模态情绪识别（IMER）任务，定向评测模型在多粒度模态/情绪信息缺失下的泛化性与鲁棒性
2. 构建MIME基准，包含2000条标注视频片段，覆盖细粒度人脸细节退化、严重人脸退化、极端全模态丢失三类真实场景
3. 提出Chain of Emotion（CoE）分析范式，配套定制化指标拆解MLLM的细粒度情绪线索感知与推理全流程
### 关键结果
对7款主流MLLM的评测显示，人脸退化场景下肢体语言、场景上下文是核心性能补偿机制，模型基础视觉感知能力与高层认知推理能力存在显著差距
