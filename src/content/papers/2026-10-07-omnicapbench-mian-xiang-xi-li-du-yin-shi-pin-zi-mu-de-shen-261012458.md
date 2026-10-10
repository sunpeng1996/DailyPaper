---
title: 'OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual
  Captioning'
title_zh: OmniCapBench：面向细粒度音视频字幕的深度结构化评测框架
authors:
- Zhongyu Yang
- Jiale Tao
- Ruitao Chen
- Zuhao Yang
- Yingfang Yuan
- Xueliang Zhao
- Auden
- Kai Wang
- Shuai Shao
- Biao Wang
affiliations:
- Hunyuan, Tencent
- Nanyang Technological University
- Northumbria University
arxiv_id: '2610.12458'
url: https://arxiv.org/abs/2610.12458
pdf_url: https://arxiv.org/pdf/2610.12458
published: '2026-10-07'
collected: '2026-10-10'
category: Eval
direction: 多模态大模型 · 音视频字幕评测
tags:
- MLLM
- Evaluation
- Audio-Visual Captioning
- Multimodal
- Benchmark
one_liner: 提出将音视频字幕评测转为原子可校验单元打分的深度结构化框架，解决现有评测覆盖与定位难兼顾的问题
practical_value: '- 多模态生成类业务（如商品短视频自动配文案、直播口播字幕校验）的评测可复用「原子校验单元+确定性规则约束+局部LLM语义比对」架构，解决全量LLM打分不稳定、漏局部错误的问题

  - 做生成内容错误归因时，可参考拆分实体、时序、跨模态对齐三类错误维度的思路，快速定位模型短板，针对性优化迭代

  - 构建自定义生成任务评测集时，可参考将自由文本预测目标转为结构化可校验单元的设计，降低评测成本同时提升结果可信度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频字幕评测存在三类核心缺陷：全字幕整体打分无法定位局部错误、局部探针法覆盖度不足、无约束LLM裁判结果不稳定，无法支撑多模态大模型音视频推理能力的细粒度诊断。
### 方法关键点
将字幕评测目标从自由文本比对转为三类原子可校验单元的结构化打分：实体引用、视觉镜头、音频事件；先通过确定性规则校验结构、时序关联，再调用局部LLM做限定范围的语义比对，同时兼顾评测覆盖率、错误定位能力、结果稳定性。
### 关键结果
基于786条密集标注音视频构建基准，可精准识别时序 grounding 失败、实体漂移、跨模态错位、幻觉四类MLLM感知错误；对前沿MLLM评测发现其局部感知能力强但长时序音视频推理能力弱，实体漂移、跨模态错位类错误占比最高。
