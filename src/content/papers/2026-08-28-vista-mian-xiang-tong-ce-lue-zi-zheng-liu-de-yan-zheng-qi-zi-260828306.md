---
title: 'VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation'
title_zh: VISTA：面向同策略自蒸馏的验证器感知学生到教师自适应方法
authors:
- Zewen Ding
- Zezhong Wu
- Zhou Tao
- Shida Wang
- Shizhuo Hou
- YongXiang Hua
- Haoyu Cao
- Linli Xu
affiliations:
- University of Science and Technology of China
- State Key Laboratory of Cognitive Intelligence
arxiv_id: '2608.28306'
url: https://arxiv.org/abs/2608.28306
pdf_url: https://arxiv.org/pdf/2608.28306
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: 大语言模型训练 · 自蒸馏优化
tags:
- Self-Distillation
- On-Policy Training
- Knowledge Distillation
- Verifier
- LLM Reasoning
one_liner: 在同策略自蒸馏中引入双向监督，基于验证通过的学生轨迹自适应优化教师模型，提升推理能力
practical_value: '- 电商客服Agent、商品文案生成的小模型蒸馏场景，可复用验证器门控逻辑，仅用业务指标达标的样本更新教师模型，避免错误信号干扰

  - 双向蒸馏的选择性更新trick可直接复用：仅选师生KL divergence最大的top-k token更新教师，既修正错位信号又保留教师原有知识，无额外采样开销，适合算力有限的业务场景

  - 导购路径规划、活动规则解读等推理类Agent训练，可复用OPSD+VISTA框架，相比GRPO等RL方法省掉奖励模型标注成本，仅用结果验证即可提升推理准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有On-Policy Self-Distillation（OPSD）默认特权教师的分布永远优于学生，仅做单向教师到学生的监督，但带参考信息的教师经常输出依赖参考的无效token，或压制学生的正确推理路径，反而误导学生训练，在数学、代码、规则理解等推理场景下问题尤为突出。

### 方法关键点
- 保留标准OPSD的学生更新逻辑，新增轻量教师更新分支实现双向监督，无需额外采样或独立奖励目标，推理阶段仅部署学生模型无额外开销
- 结果门控：只有学生生成的rollout通过结果验证（如答案正确、代码跑通测试用例）时，才允许用该rollout更新教师
- 选择性更新：对符合条件的rollout，仅选师生KL divergence最大的top-k个token位置，用反向KL让教师向学生分布对齐，避免教师过快收敛到学生丢失原有特权知识

### 关键实验
在AIME24、AIME25、HMMT25三个数学推理benchmark上，用Qwen3 1.7B/4B/8B三个尺度测试，对比Base、SFT、GRPO、SDPO、标准OPSD：VISTA在三个尺度下Avg@12分别比OPSD提升0.6、0.7、2.1个点，9个尺度-基准组合中8个达到SOTA，其中8B尺度提升最显著，AIME25提3.1个点，HMMT25提2.5个点。

**最值得记住的一句话**：同策略自蒸馏中的特权教师不是永远正确的，用验证通过的学生推理信号反向优化教师，能以极低额外成本实现师生互相促进的正向循环
