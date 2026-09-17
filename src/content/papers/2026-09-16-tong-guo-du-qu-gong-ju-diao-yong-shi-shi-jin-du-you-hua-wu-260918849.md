---
title: 'Ask the Tool, Don''t Guess: Agent Tool Calls Hold Their Progress, and the
  Serving System Should Read It'
title_zh: 通过读取工具调用实时进度优化Agent服务的KV缓存调度
authors:
- Yipeng Liu
- Yingqiang Zhang
- Feifei Li
- Huanchen Zhang
affiliations:
- Tsinghua University
- Zhejiang University
- Alibaba Cloud Computing
arxiv_id: '2609.18849'
url: https://arxiv.org/abs/2609.18849
pdf_url: https://arxiv.org/pdf/2609.18849
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent服务 · KV缓存调度优化
tags:
- Agent Serving
- KV Cache
- Tool Call
- LLM Inference
- Scheduling
one_liner: 通过无侵入侧信道获取Agent工具实时运行进度，大幅提升KV缓存调度效率，降低首Token延迟
practical_value: '- 工具调用阶段的KV缓存调度无需依赖预训练时长预测模型，可通过侧信道抓取工具实时进度（命令行输出、文件生成状态等），完全不影响Agent输入的前提下提升调度精度

  - 对于包含大量长耗时工具调用的Agent系统（如商品合规审核Agent、用户工单处理Agent），可直接复用论文的harness设计，实现p90 TTFT降低20%+的收益

  - 可借鉴信用机制处理自定义工具的进度造假问题，根据历史上报准确率动态调整调度权重，避免恶意占用GPU资源

  - 优化重心放在占总耗时60%+的长尾长耗时调用上，短耗时调用直接用LRU策略即可，投入产出比最高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent服务系统调度KV缓存时，仅能基于工具名、历史调用时长等静态信息猜测工具运行时长，准确率极低；尤其是占总工具时间2/3以上的长尾长耗时调用，时长受环境负载、远程API波动影响极大，预测结果甚至无法对调用时长排序，导致KV缓存被无效占用，工具调用后的首Token延迟（TTFT）高企。

### 方法关键点
- 设计无侵入harness层，通过独立侧信道读取工具运行进度，完全不修改Agent的输入输出：恢复被屏蔽的进度条输出、添加verbose开关后将进度信息从返回结果中剥离、监控执行环境的文件生成状态、给Agent生成的脚本自动插入进度上报代码
- 进度信号分为两类：强信号（明确剩余工作量占比）、弱信号（仅能感知调用即将结束），两类信号均可用于KV缓存的保留/逐出/预取决策
- 加入信用机制，对上报进度的准确性进行记账，恶意虚报的会话取消进度调度权限，避免资源浪费

### 关键结果
在mini-SWE-agent、OpenHands、Qwen 3.8 Flash等4个公开Agent语料集上测试，对比LRU、Continuum、CacheWise等4种现有调度器：进度上报的剩余时长估计误差比最优基线低3~10倍；p90 TTFT相比LRU降低20.7%（仅HBM）、20.8%（HBM+DRAM），性能接近理想Oracle。

**最值得记住的一句话**：服务系统不要去猜工具能直接告诉你的信息。
