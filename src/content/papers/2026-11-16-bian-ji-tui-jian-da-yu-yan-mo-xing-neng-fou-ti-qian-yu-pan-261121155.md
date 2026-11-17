---
title: 'Edit Recommendation: Can LLMs Anticipate Edit Requests from Users, and When?'
title_zh: 编辑推荐：大语言模型能否提前预判用户的编辑请求
authors:
- Daisuke Kikuta
affiliations:
- NTT, Inc.
arxiv_id: '2611.21155'
url: https://arxiv.org/abs/2611.21155
pdf_url: https://arxiv.org/pdf/2611.21155
published: '2026-11-16'
collected: '2026-11-17'
category: QueryRec
direction: Query推荐 · LLM会话编辑请求预判
tags:
- LLM
- Query Recommendation
- Conversational Agent
- Benchmark
- Gating Mechanism
one_liner: 提出编辑推荐任务与评测基准EditRecBench，通过决策模型门控提升编辑建议准确率
practical_value: '- 电商客服Agent、AI文案生成工具可复用编辑预判逻辑，提前透出用户可能的修改选项，降低用户交互成本，提升使用体验与转化效率

  - 面向低确定性的推荐/预判场景可引入决策模型门控机制，过滤低置信度结果，大幅提升透出内容的准确率，避免无效推荐打扰用户

  - 构建业务场景的个性化推荐/预判评测集时，可参考从真实交互日志清洗标注的思路，保证评测结果贴合实际业务表现'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM Agent生成内容后用户需手动输入编辑请求，交互成本高，业界缺乏该预判任务的标准化评测与落地方案
### 方法关键点
1. 正式定义编辑推荐任务，基于WildChat-4.8M真实对话日志构建开源评测基准EditRecBench
2. 针对真实场景下部分编辑请求难以预测的问题，引入决策模型门控机制，提前过滤低置信度预测结果再透出给用户
### 关键结果
训练得到的门控模型效果优于现有决策模型，在设定门控阈值下，透出推荐的pass@5提升12~25个百分点
