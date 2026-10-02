---
title: 'JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces'
title_zh: JevSpawn：基于组合动作空间的自适应智能体推理
authors:
- Haoyang Su
- Weiran Huang
affiliations:
- Fudan University
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2610.00437'
url: https://arxiv.org/abs/2610.00437
pdf_url: https://arxiv.org/pdf/2610.00437
published: '2026-09-29'
collected: '2026-10-02'
category: Agent
direction: Agent 推理效率与效果优化
tags:
- LLM-Agent
- Inference-Optimization
- Action-Space
- Parallel-Inference
- Low-Latency
one_liner: 提出无需额外训练的组合式Agent推理框架，同时提升任务效果与推理速度
practical_value: '- 电商导购/推荐Agent可复用组合动作空间设计：将常用工具调用（商品检索、优惠券查询、订单查询等）抽象为有限字段组合，替代逐token生成动作，降低推理延迟

  - 多候选生成场景可复用前缀共享+批量有限值评估机制：比如个性化内容/文案生成的多候选并行打分，共享上下文KV cache，减少重复计算开销

  - 复杂用户query处理可参考反馈驱动分支选择+回溯机制：保留高概率候选分支，失败时无需重新生成全链路上下文，直接回溯重试，提升处理成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent逐token生成推理与动作，多分支探索计算开销极高；Jev类有限域预测速度快但依赖预定义动作空间，无法适配自主任务求解时动作空间动态推导的需求，亟需兼顾推理效率与动作空间灵活性的方案。
### 方法关键点
- 组合式动作表示：自动将自然语言任务规则解析为带依赖的有限字段集合，字段值组合映射为可执行动作，无需预定义动作空间
- 自适应分支探索：基于Jev风格有限概率并行生成多动作分支，结合执行反馈剪枝无效分支、修订动作空间，保留候选分支支持失败回溯
- 并行计算优化：共享动作结构与上下文前缀，批量评估有限字段值概率，避免重复生成动作字符串与上下文计算，全程无需额外训练
### 关键结果
基于Qwen3.8-27B底座，在8个基准任务（路径规划、迷宫导航、解谜、数值游戏等）上对比LATS、LLMCompiler等7个主流Agent基线：
- 效果：5/8任务得分最优，迷宫/网格导航成功率达0.96/0.95，远超次优基线的0.52/0.73；2048游戏得分305.12，是次优基线的61倍
- 效率：平均端到端延迟比最快基线低15.6%，迷宫/网格导航延迟分别降至40.91s/40.58s，远低于次优基线的47.91s/61.44s；文本解码吞吐量最高达580 tok/s
> 最值得记住：无需额外训练的组合式有限动作空间推理，是平衡Agent效果与延迟的高性价比路径
