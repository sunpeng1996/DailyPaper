---
title: 'You Shouldn''t Have Asked: A Pragmatics-Inspired Taxonomy for Evaluating LLM
  Refusals'
title_zh: 基于语用学的大语言模型拒绝行为分类框架与评估
authors:
- Ruoxuan Li
- Pinqiao Wang
- Sheng Li
- Cameron Robert Jones
affiliations:
- Stony Brook University
- University of Virginia
arxiv_id: '2608.30856'
url: https://arxiv.org/abs/2608.30856
pdf_url: https://arxiv.org/pdf/2608.30856
published: '2026-08-31'
collected: '2026-09-02'
category: Eval
direction: LLM安全评估 · 拒绝行为语用学分类
tags:
- LLM Safety
- Refusal Evaluation
- Pragmatics
- LLM Alignment
- User Experience
one_liner: 提出三层语用学分类框架，系统评估16款LLM在14类有害场景下的拒绝行为特征与问题
practical_value: '- 电商导购/客服Agent的拒绝话术设计可复用三层分类框架：针对违规请求（如索要隐私、恶意砍价）优先用政策导向理由而非道德评判，搭配共情表达+合法替代方案（如优惠券），避免激怒用户降低流失

  - Agent安全对齐训练可扩展该框架的维度作为评估指标：除了判断是否正确拒绝，还要考核拒绝话术的友好性，平衡安全合规与用户体验

  - 业务场景的拒绝话术效果评估可直接复用LLM-as-judge标注流程：选择GPT-5.5这类强模型作为自动标注器，标注准确率与人类一致性可达kappa 0.85以上，大幅降低人工标注成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM安全对齐仅关注是否拒绝有害请求，忽略拒绝话术的语用影响：生硬的道德评判式拒绝会伤害用户体验、引发对立，在自伤等敏感场景甚至会加重用户心理负担，此前缺乏统一的语用学维度的拒绝行为评估框架。
### 方法关键点
- 三层语用学分类框架：Layer0判断请求合规性（完全/部分/不合规），仅不合规请求进入后续分层；Layer1标注拒绝理由（无理由/能力不足/政策限制/伦理道德），区分责任归属；Layer2标注拒绝实现策略（显式/隐式）+12类辅助语用特征（道歉、共情、负面评判、替代方案等）
- 测试集覆盖14类伤害场景，共200条prompt，调用16款主流LLM生成3200条回复做批量分析
- 验证了GPT-5.5作为自动标注Judge的可靠性，可规模化处理大规模标注需求
### 关键结果数字
- 整体请求合规率21%（17%完全合规，4%部分合规），77%请求被拒绝；暴力/性犯罪类请求拒绝率达92%以上，专业建议类拒绝率仅47%
- 70%的拒绝以伦理道德作为核心理由，仅6%归因于政策限制、1%归因于能力不足，23%为无理由生硬拒绝
- 90%的拒绝为显式直接拒绝，几乎无模糊空间，但道歉/缓冲话术占比极低，无模型使用软化模糊措辞；自伤类敏感场景下，负面道德评判占比仍高达40%
- 2024到2026年OpenAI、Anthropic的主流模型拒绝时的道歉率从90%以上暴跌到0-4%，拒绝话术整体趋于生硬
### 核心结论
LLM的安全拒绝不仅要清晰划清合规边界，更要避免道德优越感式的居高临下，在合规的同时兼顾用户的情绪与体验
