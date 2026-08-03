---
title: 'TokTier: Exact Stateful Tokenization for Agentic LLM Serving'
title_zh: TokTier：面向Agent LLM服务的有状态精确分词方案
authors:
- Zhenyu Zhang
- Zhichao Cao
affiliations:
- Arizona State University
arxiv_id: '2607.29678'
url: https://arxiv.org/abs/2607.29678
pdf_url: https://arxiv.org/pdf/2607.29678
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: LLM推理优化 · 有状态分词
tags:
- LLM Serving
- Tokenization
- Agent
- GPU Acceleration
- KV Cache
one_liner: 面向Agent类增量请求场景，实现100%精确、速度最高提升数百倍的有状态分词服务
practical_value: '- 电商导购Agent、广告生成Agent等长会话服务可直接复用增量分词思路：会话留存历史分词结果，仅对增量+末尾小窗口重分词，配合稳定边界检查保证输出和标准分词完全一致，可大幅降低长会话分词开销，提升首Token响应速度

  - 生成式推荐prompt批量处理、广告文案批量Embedding等大流量长文本分词场景，可借鉴GPT系分词的run-local并行改造方案，用GPU实现100%精确的分词加速，比CPU方案快数十倍，降低算力成本

  - 生产环境部署分词优化方案时，可复用shadow verifier采样校验机制：对少量流量用标准分词器校验优化方案输出，避免近似方案导致的KV cache失效、模型输出偏移等业务风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM服务普遍通过KV cache复用降低长会话推理开销，但前端分词仍每次全量重算，在Agent类场景下浪费尤为突出：这类场景94%以上的请求是会话增量，仅追加约1.4K字符，但上下文可达百万字符；当KV cache命中率接近0.99时，分词开销占首Token时间的比例从10%升至64%，成为核心瓶颈。
### 方法关键点
- 有状态增量分词：保留会话的历史分词结果与字节跨度，收到增量请求时仅重分词增量+旧内容末尾512字符的窗口，匹配一致后检查稳定边界（预分词器规则下不受右侧文本影响的字符类转换点），检查通过则拼接结果，失败则扩大窗口直至全量重分词，保证输出与标准分词完全一致
- GPU精确全分词：将GPT系的串行正则预分词拆解为字符分类、最大同类别-run提取、局部规则判断的并行流程，配合按片段长度优化的GPU BPE kernel，实现100%和标准分词对齐的GPU加速
- 正确性校验：后台采样流量用标准分词器校验输出，覆盖历史依赖类实现BUG，避免线上故障
### 关键结果
测试覆盖17类生产分词器、12.4TB真实语料、9.3万+Agent步，分词输出0偏差。增量分词在1M字符上下文下耗时0.5-1.1ms，比HF分词快437倍，比最优缓存基线GigaToken快2.1倍。GPU全分词处理1M字符请求耗时0.87ms，比HF分词快491倍，比现有最快CPU方法快23.4倍。搭配vLLM时，负载场景下首Token中位数降低16-34%，P99降低23%；50ms P99目标下，4核修复池+1张GPU支持1821请求/秒，是16核无状态CPU前端的45倍。
### 核心结论
在Agent长会话场景下，分词的优化空间远大于多数人的预期，且完全可以在不牺牲正确性的前提下实现数量级的性能提升
