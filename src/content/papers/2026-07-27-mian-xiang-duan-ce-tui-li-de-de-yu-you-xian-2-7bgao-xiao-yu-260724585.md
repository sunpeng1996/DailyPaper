---
title: 'From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for
  Mobile Inference'
title_zh: 面向端侧推理的德语优先2.7B高效语言模型ELMOD
authors:
- Darina Gold
- Alexander Schwirjow
- Viktor Haag
- Viktor Hangya
- Joel Schlotthauer
- Fabian Küch
- Luzian Hahn
affiliations:
- IIS Fraunhofer
arxiv_id: '2607.24585'
url: https://arxiv.org/abs/2607.24585
pdf_url: https://arxiv.org/pdf/2607.24585
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: 小参数量LLM · 端侧推理优化
tags:
- On-Device-LLM
- Small-LLM
- Low-Compute-Training
- Multilingual-LLM
- Data-Preprocessing
one_liner: 仅用公开数据与55k H100算力训出2.7B德语端侧LLM，性能追平同语种7B模型
practical_value: '- 端侧推荐/Agent场景训垂直小LLM时，可复用「数据预过滤+质量重写」流程，在有限算力下提升小模型训练效率与最终性能

  - 面向小语种（如东南亚、欧洲小语种电商）做LLM适配时，可参考其针对语言特性（形态、复合词、拼写）定制预处理的思路，降低训练成本

  - 小参数量端侧LLM训练可复用其算力优化方案，仅用公开数据即可接近大参数量模型的垂直效果，降低端侧部署门槛'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
大参数量LLM依赖云端部署，存在隐私泄露、推理延迟高、合规难满足等问题，现有<3B小参数量模型对德语等非英语语种适配差，不符合欧盟AI法案透明性要求，缺少低成本训练方案。
### 方法关键点
1. 定制德语专属预处理流程，针对德语的形态变化、复合词、拼写规则做适配，区别于通用英文预处理逻辑；
2. 新增数据质量过滤与重写步骤，提升指令数据质量，优化训练退火阶段性能，降低整体算力消耗；
3. 全程仅使用公开数据集训练，算力预算控制为55k H100 GPU小时。
### 关键结果
2.7B参数量的ELMOD为同量级（<3B）德语模型中性能最优，效果追平同场景7B参数量模型，适配端侧资源受限硬件部署。
