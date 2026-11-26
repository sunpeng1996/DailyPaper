---
title: 'Demystifying the Autoresearch Harness: How Context and Skills Shape Self-Evolving
  Agents'
title_zh: 拆解自演进研究Agent框架：上下文与技能管理的设计规律
authors:
- Kelvin Kiu-Wai Tam
- Newt Hue-Nam K. Nguyen
- Tianshi Zheng
- Yunxiang Mo
- Weihan Li
- Zhongwei Xie
- Chiu Yeung Tang
- Jui-Yu Ho
- Yangqiu Song
- Ginny Y. Wong
affiliations:
- The Hong Kong University of Science and Technology
- The University of Tokyo
- National Taiwan University
- NVIDIA AI Technology Center
arxiv_id: '2611.28244'
url: https://arxiv.org/abs/2611.28244
pdf_url: https://arxiv.org/pdf/2611.28244
published: '2026-11-19'
collected: '2026-11-26'
category: Agent
direction: 长周期自演进Agent 内存管理设计
tags:
- Self-Evolving Agent
- Context Management
- Skill Management
- Long-Horizon Agent
- Autoresearch
one_liner: 通过受控实验验证上下文折叠+过期技能删除是长周期自演进Agent的最优内存设计
practical_value: '- 长周期迭代类Agent（如推荐系统自动调优Agent、广告素材迭代Agent）可直接复用上下文折叠方案：给每轮尝试生成1行摘要，按需展开完整记录，既能保留更多历史信息，又比截断基线省34%左右的上下文token

  - 技能库管理优先采用删除策略：设置连续N轮（论文用5轮，业务可根据迭代周期调整）未被调用就自动删除，比技能合并、规则晋升的平均收益高1.1~1.9pct，还能避免冗余技能挤占检索空间

  - 不同基座的技能调用习惯差异大：开源大模型平均每轮调用6~7个技能，闭源GPT-6系列仅调用0.5~2个，业务适配时要根据基座能力调整技能库的规模和召回阈值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自演进研究Agent的框架多为多组件耦合设计，无法单独量化上下文管理、技能管理等内存模块的真实收益，长周期迭代时存在历史溢出上下文窗口、技能库冗余噪声两大核心痛点，缺乏经过受控验证的统一设计规范。
### 方法关键点
- 基线采用最近截断策略：历史长度溢出时丢弃最早尝试，技能库只新增不删除
- 对比2种上下文管理方案：折叠（每轮尝试生成可展开摘要，按需恢复完整内容）、压缩（老旧历史合并为滚动摘要，不保留单条尝试记录）
- 对比3种技能管理方案：删除（连续5轮未被调用的技能自动移除）、合并（语义相似度≥0.8的技能合并去重）、晋升（经校验有效的技能转为全局规则）
### 关键实验结果
在MLE-Bench（Kaggle ML竞赛）、KernelBench（CUDA内核优化）两个基准，覆盖3款不同基座测试：上下文折叠比基线最高提升19.2%，平均提升8.6%；技能删除比基线平均提升4.1%；组合两个最优策略的MLEvolver，在MLE-Bench Lite奖牌率达72.7%（相对AIDE提23%、相对OpenEvolve提14%），KernelBench L3 fast1得分达94%（相对AIDE提21%、相对OpenEvolve提34%）。
### 核心结论
长周期自演进Agent的内存管理核心是「保留所有历史的可寻址性+动态淘汰无效技能」，盲目做历史压缩或技能固化反而会降低迭代效率。
