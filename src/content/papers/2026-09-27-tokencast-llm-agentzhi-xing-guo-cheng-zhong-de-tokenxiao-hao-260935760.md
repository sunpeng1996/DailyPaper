---
title: 'TokenCast: Forecasting Token Consumption During LLM Agent Execution'
title_zh: TokenCast：LLM Agent执行过程中的Token消耗预测框架
authors:
- Chaoqian Ouyang
- Ling Yue
- Libin Zheng
- Huanghui Guo
- Shengxiang Xu
- YiShu Wang
- Ran Li
- Jian Yin
- Shaowu Pan
- Shimin Di
affiliations:
- Sun Yat-Sen University
- Rensselaer Polytechnic Institute
- Southeast University
- Hong Kong University of Science and Technology
arxiv_id: '2609.35760'
url: https://arxiv.org/abs/2609.35760
pdf_url: https://arxiv.org/pdf/2609.35760
published: '2026-09-27'
collected: '2026-09-29'
category: Agent
direction: Agent 执行链路Token成本动态预测
tags:
- LLM Agent
- Token Forecasting
- Cost Control
- LightGBM
- Execution Optimization
one_liner: 通过可组合的执行段成本表征，无需额外LLM调用即可动态预测Agent全链路Token消耗
practical_value: '- 搭建电商Agent导购/智能客服系统时，可引入段成本拆分逻辑，动态监控多轮对话的Token消耗，避免单会话成本超支

  - 可复用其无额外LLM调用的轻量预测架构，基于历史执行轨迹训练LightGBM模型即可上线，推理延迟仅几十ms，对业务链路无性能影响

  - 预算控制场景可直接复用其动态阈值策略，相比固定预算策略平均节省21.3%Token，相同成本下可覆盖更多用户请求

  - 迁移到新Agent业务场景时，仅需20条目标域历史轨迹即可完成适配，无需重新标注大量数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent执行相同任务时Token消耗差异可达30倍，上下文不断累积导致后续调用输入成本持续膨胀，现有方法要么仅支持单调用长度预测，要么依赖额外LLM成本预估，无法适配无预设执行路径的开放Agent场景，难以支撑业务的成本管控和资源调度需求。
### 方法关键点
- 可组合的执行段成本三元组表征<调用次数n、上下文净变化g、成本残差b>，通过相邻段组合公式自动计算前序上下文对后续调用的输入成本增量
- 分层设计预测链路：单调用级支持调用前、生成中动态更新预估，任务级结合直接回归预测+前缀-后缀组合预测两条路径，再通过校正模型输出最终结果
- 全程无额外LLM调用，仅用历史执行轨迹训练LightGBM模型，支持执行过程中每完成一次调用就滚动更新剩余Token消耗预估
### 关键实验
在4个基准数据集（SWE-bench Verified、Search-R1、MMLU-Pro、LongBench-v2）、6款Agent LLM上测试，对比TRAIL、EGTP、Self-Prediction等5个基线，96组测试场景下平均MAE比最优基线低14.5%，执行中更新预测场景下MAE降低超30%；离线预算控制回放中，相同任务完成率下比固定预算策略节省21.3%Token，单次任务全链路预测总耗时仅32.8ms。
### 核心洞察
Agent Token消耗预测的核心难点是上下文累积的放大效应，拆分执行段的可组合表征远比直接端到端回归更适配动态执行的Agent场景。
