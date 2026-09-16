---
title: 'FlashVector: Agent for Hierarchical Model Serving Stack Optimization'
title_zh: FlashVector：面向分层模型服务栈优化的Agent系统
authors:
- Qi Wu
- Lohan Lemire
- Kai Meng
- Zhongmou Cai
- Raphael Bargues
- Petr Zhitnikov
- Zeyuan Cao
- Yao Wang
- Shujun Bian
- Wei Chen
affiliations:
- Stanford University
- Unity Vector AI Team
arxiv_id: '2609.17391'
url: https://arxiv.org/abs/2609.17391
pdf_url: https://arxiv.org/pdf/2609.17391
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent 模型服务栈全链路性能优化
tags:
- LLM_Agent
- Model_Serving
- Recommendation_System
- Performance_Optimization
- GPU_Optimization
one_liner: 将LLM驱动的单GPU内核优化范式扩展到全模型服务栈，实现跨层自动性能调优
practical_value: '- 可复用分层Agent抽象，给推荐系统的特征服务、模型服务、推理引擎分别定制Profile/Diagnose/Optimize/Verify四步接口，无需从零设计全栈优化Agent

  - 可落地「局部优化+全局校验」机制，单模块的性能优化必须经过全链路压测、生产流量回放验证，避免局部优化导致全链路SLO降级

  - 可直接复用验证规则集：确定性改写要求输出完全一致，浮点重排要求元素级绝对误差在1e-3以内，配置调优走影子流量灰度，覆盖90%以上推理优化场景的正确性校验

  - 可搭建always-on自动优化循环，在模型重训、流量波动、硬件升级后自动触发调优，解决人工优化失效快的问题，降低服务成本'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
生产推荐/广告系统的模型服务成本占比极高，全栈优化需要跨GPU内核、ML框架、模型服务、特征处理四层的专业知识，人力成本高且优化效果随模型迭代、流量漂移快速失效；现有Agent仅能做单GPU内核优化，无法覆盖全栈优化需求。

### 方法关键点
- 分层Agent抽象：每一层服务组件都实现统一的四步接口：Profile（层专属工具采样性能，如eBPF调服务、Nsight调内核）、Diagnose（结合层专属知识库定位瓶颈）、Optimize（生成代码/配置变更）、Verify（校验正确性与性能增益），最终增加Refine步骤将优化经验沉淀回知识库
- 局部优化全局校验：每层独立做优化提案，所有通过单层校验的变更必须经过全链路生产流量回放压测，仅当端到端增益超过测量噪声且满足SLO才会被采纳
- 常驻自动优化循环：无需人工触发，模型发布、流量/硬件变更后自动启动调优，基于历史优化记录迭代，避免优化效果随时间衰减

### 关键结果
在Unity Vector广告生产环境落地，对比人工优化基线：模型服务端最高实现2×吞吐量提升、1.98× latency加速，特征存储端最高实现1.6×吞吐量提升；其中Triton服务序列化逻辑优化单步提速30×，融合注意力内核提速3.56×，特征预处理Cython改写最高单步提速350×。

### 核心洞见
Agent不仅能做单点代码优化，还可以作为连接原型参考代码与高性能生产系统的中间层，自动适配异构技术栈的优化需求。
