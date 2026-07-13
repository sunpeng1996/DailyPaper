---
title: Test-Time Scaling for Small VLMs on Multilingual Visual MCQ
title_zh: 面向多语言视觉多选题的小型VLM测试时缩放优化方法
authors:
- Spiros Baxevanakis
- Peng-Jian Yang
affiliations:
- University of Amsterdam
arxiv_id: '2607.09438'
url: https://arxiv.org/abs/2607.09438
pdf_url: https://arxiv.org/pdf/2607.09438
published: '2026-07-10'
collected: '2026-07-13'
category: Reasoning
direction: 多模态推理 · 测试时缩放优化
tags:
- Test-Time Scaling
- VLM
- Multimodal Reasoning
- Self-Consistency
- PRM
one_liner: 验证小VLM测试时缩放中工程与模型选型优于复杂策略，登顶ImageCLEF 2026视觉MCQ榜单
practical_value: '- 做LLM/VLM推理优化时优先保障单链token预算充足，ROI远高于盲目增加采样条数：本文中1k→2k token涨3.7pp，8→16条采样仅涨0.15pp

  - 输出提取环节新增引导修复步骤（补Answer cue+受限解码），极低计算成本即可解决大量解析失败问题，避免把解析错误误判为推理错误

  - 7B及以下小模型的推理优化，优先升级基座模型，ROI远高于叠加PRM引导搜索、后验选择器等复杂策略：本文换基座涨11.4pp，远超其他策略收益

  - 多语言/多场景推理任务优先用简单self-consistency多数投票，复杂PRM、生成式批评家基本无增益甚至负增益，还会大幅提升推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Test-Time Scaling (TTS) 已被验证可大幅提升大语言模型推理能力，但在7B及以下开源小型VLM上的适配效果、最优策略尚不明确，且多语言多模态推理场景下的单GPU、参数上限等约束也对TTS的落地提出了实际需求。

### 方法关键点
- 对比两类开源基座：Qwen2.5-VL-7B-Instruct、Qwen3.5-4B，均在单A100-40GB上运行，采用vLLM批量并行解码+前缀缓存降低推理延迟
- 对比三类策略：describe-then-reason+PRM引导波束搜索、不同参数的Self-Consistency（SC）、三种后验选择器（多数投票、无训练生成式批评家、预训练多模态PRM）
- 新增引导解析修复：对未输出答案的推理链补`Answer:`提示+受限解码直接输出选项字母，几乎无额外成本解决解析失败问题

### 关键结果
- 基于EXAMS-V多语言视觉多选题基准（覆盖11种语言、20个学科）验证，最佳配置在ImageCLEF 2026测试集上达84.1%准确率，排名总榜第一
- 单链token预算从1k提升到2k，准确率提升3.7pp，而采样链数从8增加到16仅提升0.15pp
- PRM引导波束搜索比普通SC准确率低0.39pp，成本却是后者的8.7倍，两类后验选择器均无法超过多数投票的效果
- 基座从Qwen2.5-VL-7B换成更小的Qwen3.5-4B，同配置下准确率提升11.4pp，是所有优化手段中收益最高的

**最值得记住的结论**：对于7B及以下小模型的推理优化，工程细节（解析格式、解码预算）和基座选型的收益，远高于复杂的搜索、验证类策略
