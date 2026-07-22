---
title: 'Prompt Design at Scale: How Format, Instruction Count, and Context Length
  Shape Instruction Adherence and Hallucination in Large Language Models'
title_zh: 大规模Prompt设计：格式、指令数、上下文长度如何影响LLM指令遵循与幻觉
authors:
- Netanel Eliav
affiliations:
- Machine Human Intelligence Lab (MHIL)
arxiv_id: '2607.19257'
url: https://arxiv.org/abs/2607.19257
pdf_url: https://arxiv.org/pdf/2607.19257
published: '2026-07-21'
collected: '2026-07-22'
category: LLM
direction: LLM提示工程 · 效果影响因子量化
tags:
- prompt-engineering
- instruction-following
- hallucination
- long-context
- benchmark
one_liner: 基于两组可控实验量化三类Prompt设计要素对5款LLM的效果影响，给出落地工程参考
practical_value: '- 不要默认选用markdown作为Prompt格式，需针对业务所用的具体LLM做AB测试，比如Qwen 35B在高指令数场景下plain文本效果优于markdown，避免通用经验带来的效果损失

  - 单轮Prompt的并行指令不要超过40条，指令数达80时所有模型的完美响应率几乎归零，复杂指令可拆分到多轮交互、工具调用或后置校验流程替代

  - LLM接近上下文窗口上限时的主要失败模式是拒答而非幻觉/阿谀奉承，电商RAG、Agent超长上下文场景需针对性添加拒答兜底逻辑，无需过度投入幻觉校验算力

  - 同等效果下优先选择token开销低的格式，markdown/表格等格式比plain文本高22%~37%的token开销，效果差异不大时选plain文本可降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
工业界做Prompt设计时，格式选择、单Prompt指令容量、上下文长度上限的决策大多依赖经验，缺乏可控量化证据支撑；过往研究未同时交叉验证格式与指令数、上下文长度两个规模维度的共同影响，难以指导大规模场景下的Prompt优化。
### 方法关键点
- 构建无预训练污染的合成语料库Book of Veyra，包含8780个唯一命名实体，可固定种子复现，支持markdown、plain文本、散文、表格四种格式渲染
- 实验1：测试单Prompt指令数从10到160区间，不同格式、指令放置在系统提示/用户轮次下的指令遵循率衰减，覆盖5款不同能力层级的LLM（Claude Sonnet 5、Claude Haiku、Gemini Flash、Qwen 27B、Qwen 35B）
- 实验2：测试上下文长度从2k到512k token区间，不同格式下的召回准确率、错误前提阿谀率、不存在事实捏造率三类指标
### 关键结果数字
- 指令数达80时，所有模型、所有格式、所有放置位置的完美响应率全部归零；指令放置位置的效果影响大于格式，且方向因模型而异，无通用最优格式，Qwen 35B在高指令数下plain文本效果比markdown高4.8pp
- 上下文长度≤64k时所有格式召回率接近天花板（98%~100%），超过64k后格式差异显著，Claude Haiku在128k时plain文本召回率仅38.3%，比其他格式低48.4pp
- 全量实验中不存在事实的捏造率为0，阿谀率最高仅8.3%，接近上下文窗口时失败模式以拒答为主，最高可达89.6%

最值得记住的一句话：Prompt设计没有通用最优解，所有经验性选择都要针对业务所用模型、场景规模做针对性验证，不要盲目套用通用提示工程技巧。
