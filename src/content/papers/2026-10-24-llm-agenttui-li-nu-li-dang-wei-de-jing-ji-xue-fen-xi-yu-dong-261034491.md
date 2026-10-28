---
title: What Effort Level Should I Choose? On the Economics of Reasoning Effort in
  LLM Agents
title_zh: LLM Agent推理努力档位的经济学分析与动态调优方法
authors:
- Kaiser Sun
- Yongchan Kwon
- Zain Hasan
- Shang Zhu
- Kaitlyn Zhou
- Federico Bianchi
affiliations:
- Johns Hopkins University
- Together AI
- Cornell University
arxiv_id: '2610.34491'
url: https://arxiv.org/abs/2610.34491
pdf_url: https://arxiv.org/pdf/2610.34491
published: '2026-10-24'
collected: '2026-10-28'
category: Agent
direction: Agent 推理努力档位优化与成本控制
tags:
- LLM Agent
- Reasoning Effort
- Cost Optimization
- Inference Efficiency
- Dynamic Routing
one_liner: 测试8款模型4类基准明确推理努力成本收益，提出朴素阶梯策略降本提效
practical_value: '- 电商导购/智能客服/文案生成类LLM Agent不要盲选最高推理档位，优先采用低档位优先、失败再升级的策略，最多可省40%+推理成本且不降低效果

  - Agent成本核算需包含用户等待时间，API计费仅占总成本不到20%，等待时间的机会成本占比更高

  - 对有明确正确性校验的Agent任务（如优惠券规则计算、合规校验）可直接复用朴素阶梯策略，无需额外训练路由模型

  - 不要默认关闭推理功能降本，无推理档位会拉长Agent多轮交互路径，反而提升输入token成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流LLM API均提供推理努力档位调节功能，用户需盲选固定档位，无法评估额外推理算力的边际价值，推理投入属于典型信任品：用户仅能看到结果，无法判断购买的推理算力是否必要。固定最高档位成本极高，固定最低档位又容易出现效果下降，亟需明确不同推理档位的成本收益规律，找到更优的档位分配策略。
### 方法关键点
- 覆盖8款主流闭源/开源模型（GPT-5.6系列、Claude Sonnet 5、GLM-5.2、Kimi K3等），测试4类基准：单调用的AIME数学题、GPQA科学题，多轮Agent的Terminal-Bench终端任务、SWE-Bench Pro代码任务
- 控制任务、Prompt、Agent框架完全不变，仅调整推理努力档位，对比不同档位的任务成功率、token成本、行为轨迹差异
- 对比3类策略：固定档位、模型自主选档位、朴素阶梯策略（最低档位失败后升级最高档位）
### 关键结果
- 高推理档位整体准确率更高，但会丢失低档位可解决的任务；所有档位都能解决的简单任务上，最高档位成本是最低的42倍
- 无推理档位不代表成本最低，会让Agent多轮交互次数增加，输入token成本最高提升4.58倍
- 朴素阶梯策略在所有模型和基准上效果持平或超过固定最高档位，AIME成本降25.3%，GPQA降41.5%，SWE-Bench Pro降15.5%，包含等待时间的总成本降幅更高

高推理努力不是越贵越好，档位价值高度依赖任务难度，动态分配比盲选最高档位性价比高得多
