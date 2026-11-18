---
title: 'Storing the Gemma 4 K=V Cache Once: Exact Global-KV Memory Savings in a Paged
  Serving Engine with Unchanged Attention Kernels'
title_zh: 无需修改注意力内核的Gemma 4全局KV缓存内存优化方案
authors:
- Kushagra Bainsla
affiliations:
- San José State University
arxiv_id: '2611.23035'
url: https://arxiv.org/abs/2611.23035
pdf_url: https://arxiv.org/pdf/2611.23035
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大模型推理 · KV缓存优化
tags:
- KV_cache
- LLM_serving
- vLLM
- Gemma
- PagedAttention
one_liner: 利用Gemma4全局层K/V结构冗余单份存储KV缓存，vLLM上吞吐量最高升38%无需修改内核
practical_value: '- 业务中使用Gemma 4系列大模型做推荐理由生成、Agent客服、营销文案生成的场景，可直接复用该方案，16位精度下KV内存降低34%~40%，吞吐量提升11%~38%，无需修改底层内核，兼容性强

  - 针对其他存在K/V结构冗余的大模型，可复用「单份存储+双视图读取+权重折叠到Query」的思路，无需适配现有serving内核即可快速落地内存优化

  - 长上下文占比高的部署场景（如电商长会话推荐Agent、用户全历史行为分析）可优先落地该优化，提升单卡并发数，降低部署成本，且兼容NIXL跨卡传输、CPU offload等现有部署组件'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
KV缓存是大模型长上下文推理的核心内存瓶颈，直接决定单卡可承载的并发请求数与吞吐量。Gemma 4全局注意力层原生设计了K与V的结构关联，理论可降低37.5%的KV缓存占用，但现有开源serving引擎未利用该冗余，仍存储完整的K、V两份数据，内存浪费严重。
### 方法关键点
- 利用Gemma 4全局层V是K投影的RMS归一化结果、仅1/4维度添加RoPE的结构特点，单份存储640个值（替代原1024个），包含RoPE后的K部分与完整V
- 通过两个重叠的步长内存视图，让原生PagedAttention内核直接读取K、V，无需修改任何底层注意力内核代码
- 将K的归一化权重折叠到Query的未旋转部分，最终用固定置换恢复输出维度顺序，算术等价无精度损失
- 仅通过Python层Hook与包装器适配vLLM块管理逻辑，侵入性极低
### 关键实验
基线为原生vLLM，测试模型为16位Gemma 4 31B：
1. 单A100 32K/64K上下文场景下，单请求稳定解码KV内存分别降低34%/40%，32K上下文eager模式吞吐量提升24%
2. 双A100预填充/解码拆分部署，16K/8K提示词场景下解码每步Token数分别提升38%/24%，eager吞吐量分别提升30%/11%
3. 精度测试仅2/432个最终答案与基线有差异，属于运行噪声范围，无业务可感知的精度损失

对于存在KV结构冗余的大模型，无需修改底层注意力内核，仅通过内存视图复用与权重折叠即可实现无损KV内存节省，可直接落地提升serving性能
