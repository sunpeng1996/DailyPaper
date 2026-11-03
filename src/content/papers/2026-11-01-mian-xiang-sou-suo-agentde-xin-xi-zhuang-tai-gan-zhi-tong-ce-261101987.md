---
title: 'Same Trajectory, Different Knowledge: Information-State-Aware On-Policy Distillation
  for Search Agents'
title_zh: 面向搜索Agent的信息状态感知同策略蒸馏方法
authors:
- Minhao Sun
- Xian-Ling Mao
- Eric Tao
- Zi-Ao Ma
- Zhijing Wu
affiliations:
- Beijing Institute of Technology
- Huawei
arxiv_id: '2611.01987'
url: https://arxiv.org/abs/2611.01987
pdf_url: https://arxiv.org/pdf/2611.01987
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: 搜索Agent 信息状态感知同策略蒸馏
tags:
- Search Agent
- On-Policy Distillation
- Policy Optimization
- Knowledge Estimation
- Question Answering
one_liner: 提出ISA-Distill解决搜索Agent同策略蒸馏的信息状态不匹配问题，提升准确率与检索效率
practical_value: '- 训练电商导购、客服类搜索Agent时，可借鉴事实可恢复性评估逻辑，根据Agent当前已掌握信息动态分配检索资源，避免单跳场景冗余检索、多跳场景检索不足的问题

  - 同策略蒸馏训练中，可复用双视角教师反馈框架：学生模型对知识掌握度高时用fact-use视角引导知识应用，掌握度低时用evidence-seeking视角引导信息获取，避免信息状态不匹配导致的反馈偏差

  - 事实可恢复性的评估方法可直接复用：对学生当前状态下发masked探针采样32次响应计算平均NLL，映射为0-1的掌握度得分，可适配不同基座模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前同策略蒸馏（OPD）训练搜索Agent时，教师会额外获取支撑证据、参考答案等特权信息，导致教师与学生的信息状态不匹配——教师可直接调用学生无法恢复的事实，会低估帮助学生获取缺失信息的检索动作的价值，最终导致学生策略出现检索不足或冗余的问题。

### 方法关键点
- 构建动作相关的焦点事实与masked探针，用冻结的rollout策略在不检索的情况下采样32次探针响应，计算平均NLL并映射为0-1的事实可恢复性得分k，代表学生当前对该事实的掌握程度
- 设计双视角教师反馈：事实使用（fact-use）视角给教师提供焦点事实，引导学生应用知识；证据搜索（evidence-seeking）视角仅给出信息需求，引导学生获取证据，两个视角的反馈按k加权（k高时偏事实使用，k低时偏证据搜索）
- 加权后的反馈作为调整项加入GRPO的优势估计，保留原结果奖励的符号，仅调整梯度幅度，仅对检索、结论相关的关键token生效

### 关键结果
在7个QA benchmark（含单跳NQ、TriviaQA，多跳HotpotQA等）上对比EviSD、SD-Search等10+基线，Qwen2.5-7B基座下宏观平均EM达48.0%，比最优基线高0.8个百分点；单跳任务检索调用减少7.21%，多跳任务检索调用增加2.94%，总检索量下降2.45%，训练耗时仅增加4.3%。

最值得记住的一句话：搜索Agent的训练反馈必须匹配学生当前的信息状态，引导其应用已掌握的知识、检索缺失的知识，才能在提升准确率的同时优化检索效率。
