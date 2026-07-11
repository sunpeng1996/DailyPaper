---
title: 'Validity of LLMs as data annotators: AMALIA on authority'
title_zh: 大语言模型作为数据标注工具的有效性：以AMALIA权威标注任务为例
authors:
- Manuel Pita
affiliations:
- Artificial Intelligence, Social Interaction and Complexity Laboratory
- CICANT, Universidade Lusófona
arxiv_id: '2607.08731'
url: https://arxiv.org/abs/2607.08731
pdf_url: https://arxiv.org/pdf/2607.08731
published: '2026-07-09'
collected: '2026-07-11'
category: Eval
direction: LLM标注有效性评估
tags:
- LLM Annotation
- Validity Evaluation
- Prompt Decomposition
- Multilingual LLM
- Reliability
one_liner: 提出恢复间隙指标验证LLM标注有效性，发现小参数葡萄牙语大模型标注依赖表面特征捷径
practical_value: '- 做LLM标注类任务（用户评论打标、query意图标注、商品属性标引）时，不能仅看和人工标注的一致性，要补充逻辑验证环节，避免模型靠表面特征匹配得到虚高准确率

  - 可直接复用「恢复间隙」方法：将原任务prompt拆解为标注规则原子子句后按逻辑重组，对比前后性能差，快速定位LLM是否依赖shortcut，提升标注Pipeline鲁棒性

  - 小参数垂直/小语种LLM落地标注任务时，优先做跨模型/跨场景迁移验证，不要直接用于核心业务标注，可先用于粗筛预标注环节降本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM标注效果评估仅关注与人工标注的一致性（可靠性），无法判断模型是真的理解任务逻辑还是靠表面特征shortcut得到高一致性，小参数国家/垂直领域LLM的标注有效性缺乏可落地的验证方法。

### 方法关键点
提出**恢复间隙（recovery gap）**指标：将整体任务prompt拆解为标注规则的原子子句，按理论规则重组后执行任务，对比与原prompt的性能差值；若校准可缩小该间隙则标注逻辑可跨模型/语言迁移，否则说明模型依赖shortcut。

### 关键结果数字
- 9B参数葡萄牙语AMALIA模型标注权威类道德基础任务，与人工标注F1仅比参数大8~13倍的开源模型低6个点
- 拆解prompt后AMALIA性能仅恢复原整体效果的50%左右，证明其依赖权威人物附近的道德愤怒等表面特征
- 同语料同prompt下开源多语种大模型可完全闭合恢复间隙，排除语料导致的性能问题
