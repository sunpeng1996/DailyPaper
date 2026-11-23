---
title: 'Beyond Prompt Heuristics: Assessing Child Safety Alignment in LLMs'
title_zh: 超越提示启发式：大语言模型儿童安全对齐能力评估
authors:
- Anika Misra
- Chimaobi Okite
- Rada Mihalcea
affiliations:
- University of Michigan
arxiv_id: '2611.26965'
url: https://arxiv.org/abs/2611.26965
pdf_url: https://arxiv.org/pdf/2611.26965
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM安全对齐 · 儿童场景评估
tags:
- LLM Safety
- Alignment Evaluation
- Child Safety
- Prompt Cues
- Activation Patching
one_liner: 揭示现有LLM儿童安全对齐高度依赖提示伤害线索，无线索良性请求错配率最高超80pp
practical_value: '- 面向未成年人的电商/内容推荐场景，不能仅依赖敏感词拦截机制，需对普通推荐请求（如影视/书籍/玩具咨询）额外做年龄适配的内容校验，避免输出成人向商品/内容。

  - 搭建LLM安全评估体系时，需扩充无明显伤害线索的测试用例，现有仅覆盖显式敏感请求的基准会大幅高估模型的实际对齐效果。

  - 做用户属性感知的LLM对齐训练时，不能仅喂带敏感词的负例，需在大量无敏感词的个性化请求（如明确用户为未成年人的推荐请求）中加入对齐约束，避免模型仅靠词汇触发安全机制。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM儿童安全对齐评估大多基于带显式伤害类别线索的提示，无法反映模型在看似良性、无敏感词的普通请求（如影视推荐）中的安全表现，而这类场景是未成年人与LLM交互的高频场景，其对齐缺陷极易被现有评估体系忽略。

### 方法关键点
- 划分两类测试请求：带伤害类别线索的cued请求（如询问电子烟购买、色情内容）、无任何线索的uncued请求（如普通影视/书籍推荐），所有请求均携带用户为未成年人的上下文。
- 引入最小变量干预：在uncued请求中仅替换单个词为伤害相关词（如`explicit`、`naughty`），控制请求意图与用户上下文不变，单独测试线索对对齐效果的影响。
- 用activation patching定位伤害线索的作用层，结合LLM-as-judge评估儿童响应错配率（CMR），3个独立法官的标注一致性达85.3%，Fleiss' κ=0.694。

### 关键结果
测试6款主流闭源/开源LLM（GPT-5.4-mini、Claude Haiku 4.5、Gemini 3 Flash、Gemma-12B、Qwen3.5-4B/27B），测试集含118条查询（43条cued、75条uncued）：
1. 所有模型uncued请求的CMR显著高于cued请求，差距最高达80.0pp（Qwen3.5-27B在cued请求错配率为0，uncued请求错配率达80%），最低也有14.7pp。
2. 仅加入1个伤害相关词，即可让5款模型的CMR下降14.7~57.3pp，对齐效果大幅提升。
3. 激活补丁实验证明，伤害线索的作用集中在LLM早期层（ lexical/semantic处理层），说明儿童安全推理高度依赖提示词的词汇关联而非上下文语义理解。

### 核心结论
现有LLM的儿童安全对齐大多是「词触发」的启发式机制，而非真正基于用户属性与内容适配的推理，仅靠显式敏感词拦截的安全方案存在巨大漏洞。
