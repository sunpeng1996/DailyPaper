---
title: Boundary-Aware Context Grounding for A Low-Channel EEG Agent
title_zh: Boundary-Aware Context Grounding for A Low-Channel
authors:
- Zhiyuan Xu
- Yueqing Dai
- Junling Li
- Junwen Luo
arxiv_id: '2606.26519'
url: https://arxiv.org/abs/2606.26519
pdf_url: https://arxiv.org/pdf/2606.26519
published: '2026-06-24'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
- Agent
one_liner: Large language models (LLMs) can make scientific software easier to use.
  However, a general mod...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Large language models (LLMs) can make scientific software easier to use. However, a general model does not automatically know which measurements a particular sensor can support, which algorithms are implemented in the current software, or which conclusions are justified by a computed result. These distinctions are especially important for low-channel electroencephalography (EEG), where sparse spatial coverage and variable signal quality make plausible but unsupported interpretations easy to produce. We present NeuraDock Agent, an open-source architecture that separates a deterministic local EEG engine from a hardware-aware language layer. The numerical engine parses recordings, performs quality control, executes reviewed spectral workflows, and writes machine-readable artifacts. The LLM receives only a compact, allowlisted summary and a versioned context pack. The context describes the seven-channel hardware, reviewed workflows, result fields, implementation boundaries, scientific limits, and reference cases. Raw EEG and dense per-sample arrays remain local We evaluate the system at three levels. First, 12 recordings produced identical structured results over ten numerical repetitions, and a complete Rest/Task run produced identical result, report, and figure hashes over three repetitions. Second, request-capture and failure-injection experiments confirmed the tested data boundary and preservation of local artifacts under HTTP, malformed-output, and connection failures. Third, a boundary-awareness benchmark tested 36 ordinary and adversarial questions under four context ablations and two LLMs, yielding 288 outputs.These results support hardware- and implementation-aware grounding as a practical mechanism for calibrating what an EEG agent accepts, qualifies, or refuses; they do not establish clinical validity or a validated absolute cognitive-load index.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
