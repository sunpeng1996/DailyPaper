---
title: Latent Compaction with Test-Time Training
title_zh: 基于测试时训练的KV缓存潜层压缩方法
authors:
- Yingfa Chen
- Xingyu Shen
- Chaojun Xiao
- Xu Han
affiliations:
- Tsinghua University
arxiv_id: '2610.20582'
url: https://arxiv.org/abs/2610.20582
pdf_url: https://arxiv.org/pdf/2610.20582
published: '2026-10-13'
collected: '2026-10-15'
category: LLM
direction: LLM长上下文 · KV cache压缩
tags:
- KV_cache
- Test-Time-Training
- Long-Context-Inference
- Context-Compression
- LLM-Inference
one_liner: 通过测试时训练优化文档专属KV缓存，实现高倍压缩下的长上下文推理精度保留
practical_value: '- 电商/Agent的RAG场景可直接复用该方法预压缩商品文档、用户历史长序列，32倍压缩下仍保持96.7%的检索准确率，单卡可承载的长上下文请求batch提升数倍，大幅降低推理成本

  - 三段式（高重要性preserver+高注意力anchor+最远点diversifier）KV初始化、两阶段冻结微调的策略，可迁移到用户长期行为序列压缩、Item库语义表征压缩等场景，平衡压缩率和信息保留率

  - 仅用通用文档prompt做测试时训练、无需下游任务标注数据的思路，适合电商多品类、多场景的长文档压缩需求，预计算的压缩缓存可跨query复用，成本可平摊到多次请求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM推理时KV cache显存占用过高、注意力计算延迟大，是RAG、Agent等场景落地的核心瓶颈；现有压缩方案要么依赖下游query无法提前预计算，要么高倍压缩下易丢失细粒度信息，检索精度跳水严重，无法满足电商商品检索、用户历史行为理解等对细节准确率要求高的场景需求。
### 方法关键点
- 三段式初始化：总槽位75%分配给KVZip+筛选的高重要性preserver（第一阶段训练冻结），剩余25%中25%为高注意力得分anchor、75%为最远点采样的diversifier，保证key空间覆盖度
- 两阶段测试时训练：阶段1固定preserver，拟合压缩cache与全量cache的注意力输出、log归一化值；阶段2用全量模型在通用文档prompt上的输出做蒸馏，联合优化所有cache槽位，全程模型权重冻结，无需下游问答标注
- 推理层适配：给压缩cache增加可学习注意力偏置，与后续query、生成token的原生KV做归一化加权融合，保证注意力逻辑与原生模型一致
### 关键实验
在RULER、LongBench、Phonebook Lookup三个长上下文基准测试，对比KVZip+、SnapKV、PyramidKV等SOTA压缩基线：32倍压缩下RULER准确率达96.7%，较KVZip+的40.0%提升56.7个百分点；16倍压缩下Phonebook Lookup平均准确率较KVZip+高30pct以上，效果跨Qwen3、MiniCPM5多个模型系列和尺寸通用。
### 核心结论
将KV cache本身作为可优化的神经网络参数，用无下游数据的测试时训练+自蒸馏，是高倍长上下文压缩下保留细粒度检索精度的可行路径
