---
title: 'MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research'
title_zh: MORSE：基于开放世界自动研究的流式内存设计优化
authors:
- Ce Zhang
- Jianshu Zhang
- Jinxi He
- Xiyuan Yang
- Pan Wang
- Han Liu
- Katia Sycara
- Yaqi Xie
affiliations:
- CMU
- Northwestern
- UIUC
- Pitt
arxiv_id: '2611.30011'
url: https://arxiv.org/abs/2611.30011
pdf_url: https://arxiv.org/pdf/2611.30011
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent 自动迭代系统架构优化
tags:
- Auto-Research
- Recursive Self-Improvement
- Streaming Memory
- VLM
- Video Understanding
one_liner: 提出开放世界自动研究框架，自动迭代流式VLM的内存检索策略，无需调整骨干权重
practical_value: '- BadCase自动优化可复用「故障聚类→外部搜索解决方案→候选生成→上线验证」的链路，将电商推荐/广告的线上BadCase按根因分组，自动检索学术/工程界成熟方案，降低人工迭代策略的成本

  - 两阶段迭代门控机制可直接套用到生成式推荐、Agent工作流优化：先保障效果增益达标，再推进 latency 压缩，同时严格限制质量损失阈值，平衡效果与效率

  - 读写路径拆分思路可迁移到实时流处理场景：将用户行为特征计算、语义索引构建等可复用操作迁移到数据写入阶段预执行，大幅降低搜索/推荐查询时的响应延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流式视频理解的内存管理、检索策略要么依赖人工设计迭代效率低，要么递归自进化方案只能使用预定义工具集，遇到重复故障无法复用公开的成熟解决方案，难以同时满足高准确率和低响应延迟的业务要求。
### 方法关键点
- 双模块架构：流式Solver执行内存读写、证据检索与冻结VLM推理，LLM Editor负责故障诊断、外部资源检索、策略迭代
- 开放世界研究链路：Editor将训练Trace的故障按根因聚类，检索论文、模型卡、开源代码获取解决方案，可申请新增感知工具（需审核合规性，排除测试集泄露风险）
- 两阶段迭代门控：先跑20轮精度迭代，要求正确选项概率增益达标；再跑5轮效率迭代，要求 latency 至少降低10%，且质量损失在预设阈值内
- 计算路径优化：支持将查询侧重复计算迁移到写入阶段预执行，平衡流式写入成本与查询延迟
### 关键结果
在OVO-Bench、StreamingBench、StreamBench三个公开基准上测试，使用Qwen3-VL-8B冻结骨干时，OVO-Bench准确率达75.1%，超同骨干次优方案3.1个百分点；平均推理延迟0.30s，比MemEvo快6.0×，比OASIS快3.5×。进化得到的策略可直接迁移到其他VLM，LLaVA-OneVision-2-8B无额外进化直接复用后，准确率提升16.3个百分点。
### 最值得记住的结论
递归自进化的核心不是从零创造新方案，而是学会复用已有公开解决方案，用严格的离线验证环节筛选对目标任务有效的改动。
