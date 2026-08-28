---
title: 'Calibrated Enough to Know, Not Calibrated to Act: Fabricated Evidence Makes
  LLM Agents Commit to the Unknowable'
title_zh: 校准充足能判断，决策校准不足：伪造证据使LLM Agent对不可知问题盲目承诺
authors:
- Pranav Aggarwal
affiliations:
- Independent Researcher
arxiv_id: '2608.27167'
url: https://arxiv.org/abs/2608.27167
pdf_url: https://arxiv.org/pdf/2608.27167
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent决策校准 · 不可知问题拒答
tags:
- LLM Agent
- Calibration
- Decision Making
- Fine-tuning
- Action Gate
one_liner: 证实LLM Agent决策受证据外观驱动而非内容，可通过小样本微调修复动作门控
practical_value: '- 电商/广告Agent调用外部数据时，新增knowability前置校验模块，对本质不可预测的问题（如未来30天商品销量涨跌、大促流量峰值）主动触发拒答逻辑，避免输出错误确定性结论

  - 可复用低成本门控训练方案：仅用500条左右跨领域合成随机事件样本（骰子、硬币、计时器等）做QLoRA SFT+DPO，即可为小模型装上拒答能力，且不会降低可回答问题的准确率

  - 输出格式设计需留足推理空间：强制结构化无推理槽的输出会完全废掉动作门控，电商客服、营销决策类Agent的prompt要避免过度限制输出结构

  - 校准评估不能只看输出概率，直接审计决策动作更有效：对预测类任务新增commitment率指标，统计对不可知问题的主动拒答比例，避免概率校准合格但决策失效的漏判'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
工业界默认给LLM Agent补充更多上下文会提升决策可靠性，但业务中Agent经常拿到格式专业、实际无预测价值的信息（如各类营销、行情看板），容易对本质随机不可预测的问题（如商品销量涨跌、大促转化效果）给出过度自信的错误决策，现有校准评估仅检测输出概率的准确性，无法识别这类决策层的失效。

### 方法关键点
- 构造4类不可知问题数据集（股票、加密货币、体育赛事、10天以上天气），所有问题答案本质随机不可预测，匹配同看板下的可回答问题作为对照，排除模型理解能力不足的干扰
- 梯度控制证据真实性：从无面板、真实专业面板、部分伪造指标面板到全伪造面板，保持外观格式完全一致，分离信息内容和包装形式的影响
- 用540条跨领域合成样本（骰子、硬币、计时器等无业务相关内容）对3B小模型做QLoRA SFT+DPO，训练动作门控让Agent主动拒答不可知问题
- 核心评估指标为commitment率（对不可知问题选择直接回答的比例）和Youden's J（区分可答/不可答问题的能力）

### 关键结果
- 12个前沿大模型的平均commitment率从无面板的6.5%提升到真实专业面板的54.0%，全伪造面板的commitment率为36.8%，和真实面板的37.6%统计上无显著差异
- 对不可知问题的回答Brier得分0.281，比直接输出50%的随机baseline还差，AUROC仅0.346，完全反预测
- 微调后3B模型对原股票数据集的commitment率降到0%，跨域转移到加密货币、体育、天气领域的Youden's J达62~100，可回答问题准确率保持99%以上
- 当输出格式移除推理空间时，动作门控完全失效，对不可知问题commitment率回到100%

**最值得记住的一句话：解锁LLM Agent自信决策的不是信息本身，而是信息的权威包装形式。**
