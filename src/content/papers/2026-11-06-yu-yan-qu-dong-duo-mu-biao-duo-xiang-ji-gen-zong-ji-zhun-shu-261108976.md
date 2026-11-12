---
title: 'Refer-CityFlow and M3Track: A Benchmark Dataset and Reference Framework for
  Language-Driven Multi-Target Multi-Camera Tracking'
title_zh: 语言驱动多目标多相机跟踪基准数据集Refer-CityFlow与参考框架M3Track
authors:
- Phuong T. Nguyen
- Hao Vo
- Tam Bang
- Hoang K. Tran
- Hoang-Minh Dau
- Mahshid Malazizi
- Tuan-Anh Hoang
- Mina Sartipi
- Thanh-Nam Doan
- Ngan Le
affiliations:
- University of Tennessee at Chattanooga
- University of Arkansas
- RMIT International University Vietnam
- Independent Researcher
arxiv_id: '2611.08976'
url: https://arxiv.org/abs/2611.08976
pdf_url: https://arxiv.org/pdf/2611.08976
published: '2026-11-06'
collected: '2026-11-12'
category: Agent
direction: Agent 模块化编排多模态跨相机跟踪
tags:
- LLM Agent
- Multi-Camera Tracking
- Multimodal
- Benchmark
- Module Orchestration
one_liner: 推出多相机语言驱动多目标跟踪基准及LLM Agent编排的模块化参考框架
practical_value: '- LLM Agent编排异构可插拔模块的架构可直接复用，适配搜索推荐中召回、排序、重排模块的动态调度场景，提升个性化query响应效率

  - 跨摄像头身份一致性关联的推理逻辑，可迁移到电商用户跨端（APP/小程序/网页）行为轨迹的ID对齐与拼接任务

  - 真实用户query结合标注数据构建基准的方法，可用于生成式推荐、自然语言搜索的测试集构建，提升评测真实性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有语言驱动多目标跟踪（Refer-MOT）基准仅支持单相机场景，无法适配真实摄像头网络中按自然语言查询跨相机跟踪目标的需求，现有跨视角方法直接迁移性能接近失效。

### 方法关键点
1. 构建Refer-CityFlow基准：基于CityFlow的跨相机身份标注扩充语言查询，覆盖40个路边摄像头的96段视频，包含660+身份一致的跨相机轨迹、4362条轨迹级描述、7699条查询（含1699条50位参与者采集的真实用户查询）
2. 提出M3Track模块化框架：由LLM-based Agent统一调度检测、跟踪、跨相机关联等可替换模块，支持多模态联合推理与时空关联

### 关键结果数字
在4摄像头场景的真实用户查询集上，单相机Refer-MOT模型HOTA仅为14.95-18.28，直接迁移的跨视角方法HOTA约0.05；M3Track可达44.10 HOTA、65.40 IDF1
