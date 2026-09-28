---
title: 'RayOrch: Programming and Executing Lineage-Controlled Multi-Grain Dataflows
  for Foundation-Model Data Preparation'
title_zh: RayOrch：面向大模型数据预处理的血缘可控多粒度数据流编程执行框架
authors:
- Xiaochen Ma
- Zimo Meng
- Junzhu Liang
- Youhe Jiang
- Yue Cheng
- Hao Liang
- Bohan Zeng
- Dengchun Li
- Lu Ma
- Zhengyang Zhao
affiliations:
- Peking University
- HKUST
- University of Cambridge
- Tencent Hunyuan
- Zhongguancun Academy
arxiv_id: '2609.18703'
url: https://arxiv.org/abs/2609.18703
pdf_url: https://arxiv.org/pdf/2609.18703
published: '2026-09-15'
collected: '2026-09-28'
category: Training
direction: 大模型训练 · 分布式数据预处理引擎
tags:
- Data_Preprocessing
- Distributed_System
- GPU_Scheduling
- Foundation_Model
- Lineage_Management
one_liner: 提出保留父子血缘的分布式大模型数据预处理引擎，GPU利用率与运行速度显著优于现有方案
practical_value: '- 多粒度数据处理的血缘追踪方案可复用到LLM4Rec/多模态推荐的训练数据流水线，自动关联原始物料和切分后的文本/图像/视频片段，无需手动做ID映射

  - Per Call FIFO Ready Queues的跨父节点batch策略可直接借鉴到GPU推理服务（比如RAG召回后的批量重排序、多模态特征提取），在保证输入输出顺序一致的前提下提升GPU利用率

  - 父节点级错误隔离机制可复用到大规模物料清洗流水线，单个物料处理失败不会中断全局任务，也无需额外编写失败重试和状态追踪逻辑'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
大模型训练数据预处理需将异构文档/视频转化为结构化记录，处理过程会生成数量长尾分布的子输出；现有方案要么粗粒度并行度不足，要么平展记录需业务侧自行维护血缘、重分组，开发成本高且GPU利用率低。
### 方法关键点
1. 提供声明式编程模型，支持可变基数的父子扩展与匹配gather操作，编译器提前校验配对合法性
2. 运行时全链路记录子节点归属、父节点关联、固定序号与终态，通过Per Call FIFO就绪队列跨父节点批量调度子任务
3. 基于血缘记录而非batch边界/完成顺序重构父节点结果，支持父节点级错误隔离，不影响无关任务执行
### 关键结果
- NVIDIA H20上，MinerU任务4→64卡提速15.14倍，视频流水线8→64卡提速7.82倍
- 端到端耗时较Ray Data低13.1%、较Daft低29%（MinerU任务），较Ray Data低16%（Docling任务）
