---
title: 'OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching'
title_zh: OasisKV：基于前瞻稀疏预取的超HBM容量KV缓存推理系统
authors:
- Can Xiao
- Sukmin Cho
- Junbong We
- Zhixiong Niu
- Jianyi Cheng
- Yiren Zhao
- Youngjin Kwon
- Yongqiang Xiong
- Rui Ma
- Junyi Liu
affiliations:
- Imperial College London
- KAIST
- Microsoft Research
- University of Edinburgh
arxiv_id: '2608.08097'
url: https://arxiv.org/abs/2608.08097
pdf_url: https://arxiv.org/pdf/2608.08097
published: '2026-08-07'
collected: '2026-08-11'
category: LLM
direction: LLM推理优化 · KV Cache 预取
tags:
- KV cache
- LLM Inference
- Speculative Decoding
- Prefetching
- vLLM
- Long Context
one_liner: 利用投机解码生成的前瞻token实现稀疏KV预取，大幅提升长上下文LLM推理吞吐量
practical_value: '- 做Agent长对话、长文案生成类推理服务时，可复用前瞻稀疏预取思路，结合投机解码的免费信号在损失极小精度的前提下提升单卡并发量，降低服务成本

  - 基于vLLM二次开发LLM服务的团队可直接复用其分层KV存储、异步预取流水线、按头KV映射的工程实现，快速落地长上下文推理优化

  - 采用prefill-decode架构拆分的离在线推理服务，可借鉴远程部分拉取（RPF）设计，避免全量KV跨节点传输，大幅降低首token延迟和decode节点内存开销

  - 可复用delta选择+上限驱逐策略，平衡KV拉取带宽、推理吞吐量和精度的trade-off，根据业务场景（实时/吞吐量优先）调整每步KV拉取比例'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长上下文、Agent类LLM推理负载中，KV缓存占用HBM比例过高，成为限制推理batch大小和吞吐量的核心瓶颈；现有KV预取方案要么预测准确率低、要么需要额外训练专用模型，且不支持prefill-decode解耦的部署架构，难以落地到生产级推理服务。

### 方法关键点
- 利用已有的投机解码（如EAGLE-3）生成的前瞻token作为无额外训练的预测信号，预测未来需要的KV块，平均准确率可达98.74%
- 设计三层异步流水线：top-K预测→KV选择→KV传输，各层任务并行执行，完全和前台解码计算重叠，不占用关键路径
- 新增按头KV映射层，支持不同注意力头维护独立的稀疏KV集合，无需修改vLLM原生分页KV管理逻辑，兼容原有稠密推理流程
- 针对prefill-decode解耦场景提出远程部分拉取（RPF）方案，仅传输初始解码需要的KV块和压缩key摘要，后续KV按需跨节点预取

### 关键结果
基于vLLM v0.12.0实现，在H100上测试Qwen3-8B、Qwen3-235B MoE等模型，对比原生vLLM、ShadowKV等基线：
- 单卡长上下文推理吞吐量最高提升2.1×，多GPU场景最高提升1.9×，prefill-decode解耦场景吞吐量提升2.1~2.3×
- 2048 token KV预算下，精度仅比全注意力低0.7个点，推理负载下仅损失0.1个精度点即可获得1.69×吞吐量提升
- 解耦场景下decode节点主机内存占用降低2.2~2.6×，KV admission阶段传输量降低6.5~9.7×

**最值得记住的一句话**：利用投机解码的免费前瞻信号做KV预取，是平衡长上下文推理精度、吞吐量、成本的极其实用的生产级优化方案。
