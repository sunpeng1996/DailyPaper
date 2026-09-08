---
title: 'AVENUE: Audio-Video EditiNg Understanding and Evaluation'
title_zh: AVENUE：音视频编辑理解与评估基准及框架
authors:
- Hayeon Kim
- Yoojin Jang
- Jaejun Yoo
affiliations:
- Ulsan National Institute of Science and Technology (UNIST)
arxiv_id: '2609.04253'
url: https://arxiv.org/abs/2609.04253
pdf_url: https://arxiv.org/pdf/2609.04253
published: '2026-08-31'
collected: '2026-09-08'
category: Multimodal
direction: 多模态音视频编辑基准与评估
tags:
- Multimodal Editing
- Benchmark
- Evaluation Framework
- Audio-Video
- Controllable Generation
one_liner: 推出覆盖三类编辑类型的音视频编辑基准与模态感知的专项评估框架
practical_value: '- 电商短视频/直播AI剪辑工具研发可复用模态感知评估思路，避免单模态修改时另一模态出现非预期改动，提升编辑可控性

  - 多模态生成效果评估环节可复用「指定修改内容+指定保留内容」的样本专项评估范式，评估准确率远高于通用模态盲评估

  - 音视频编辑模型迭代时可直接调用AVENUE开源基准做性能验证，快速定位不同编辑范式下的模态选择性短板'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频编辑基准覆盖的编辑类型、模态组合范围有限，主流评估方案多为模态盲、样本无关设计，无法准确校验模型是否完整保留非目标模态内容，难以衡量编辑可控性。
### 方法关键点
1. 构建AVENUE基准，包含1291条源片段、7957条人工校验的编辑指令，覆盖音频定向、视频定向、音视频联动三类编辑类型
2. 推出样本专属、模态感知的评估框架，每个样本明确标注需修改的内容与必须保留的内容边界
### 关键结果
测试联合、序列、分离三类主流音视频编辑范式，发现所有范式均存在共性缺陷：编辑单模态时会高频引发另一模态的非预期改动，是当前领域核心待解挑战。
