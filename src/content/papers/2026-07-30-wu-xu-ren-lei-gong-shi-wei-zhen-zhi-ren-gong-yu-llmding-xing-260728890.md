---
title: 'Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative
  Coding When Human Consensus Is Not Ground Truth'
title_zh: 无需人类共识为真值：人工与LLM定性编码的盲专家验证方法
authors:
- Alex Liu
- Lief Esbenshade
- Michael Xiao
- Victor Tian
- Zachary Zhang
- Kevin He
- Min Sun
affiliations:
- University of Washington
- Colleague AI
arxiv_id: '2607.28890'
url: https://arxiv.org/abs/2607.28890
pdf_url: https://arxiv.org/pdf/2607.28890
published: '2026-07-30'
collected: '2026-08-03'
category: Eval
direction: LLM能力评估 · 定性编码评估方法
tags:
- LLM Evaluation
- Text Annotation
- Human-AI Collaboration
- Qualitative Coding
- Blind Verification
one_liner: 证明对齐人类的LLM定性编码评估存在偏差，提出可迁移的盲专家验证协议与人机分工框架
practical_value: '- 做LLM辅助的用户评论、客服会话、商品标签标注时，不要完全以人工标注一致性为唯一评估标准，可引入盲专家 pairwise 对比降低人类共通偏差

  - 内部搭建LLM标注能力评估链路时，可复用本文的盲源对称评估+Bradley-Terry排序流程，更准确判断LLM标注的实际质量

  - 人机分工标注场景下，可参考本文的代码级分工框架，优先将人类共识偏差高的标注项交给LLM处理'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM辅助定性编码评估普遍以与人类标注的一致性为核心指标，默认人类标注是绝对真值，该假设的合理性缺乏实证支撑。
### 方法关键点
- 选取5套LLM系统、3名受训人工标注员，针对K12教育平台2560条educator消息，基于72项层级编码本独立标注
- 引入独立领域专家对855组盲源编码结果做对称 pairwise 评判，不告知标注来源为人工还是LLM
### 关键结果
传统一致性指标下，人-人标注Jaccard系数为0.52，人-LLM仅0.30，看似LLM表现显著更差；但盲专家偏好人工、LLM标注的比例无统计学差异（51.5% vs 48.5%，p=0.537），Bradley-Terry排序显示2个LLM表现优于3名人工标注员中的2位，且部分编码场景下人类共识存在共通偏差，专家更认可LLM的标注结果。
